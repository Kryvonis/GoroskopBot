import requests

from sqlalchemy import select

from app import db_engine
from app.core.abstract_command import AbstractCommand
from app.models.models import user
from app.settings import Config


class TelegramCommand(AbstractCommand):
    def __init__(self, msg):
        self.msg = msg
        self.text = msg['text'][msg['entities'][0]['length']:].strip()
        self.user_name = msg['from']['username']
        self.user_id = msg['from']['id']
        self.chat_id = msg['chat']['id']
        with db_engine.connect() as conn:
            res = conn.execute(select(user.c).where(
                user.c.telegram_id == self.user_id)).fetchone()
            if not res:
                conn.execute(
                    user.insert(return_rows=True).values(
                        telegram_id=self.user_id,
                        first_name=msg['from']['first_name'],
                        last_name=msg['from']['last_name'],
                        username=self.user_name,
                        language_code=msg['from']['language_code'],
                        chats=self.chat_id
                    )
                )
                res = conn.execute(select(user.c).where(
                    user.c.telegram_id == self.user_id)).fetchone()
        self.user = dict(res)

    def execute(self):
        pass

    def send_message(self, chat_id, text):
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'Markdown'
        }
        res = requests.post('{}sendMessage'.format(Config.BOT_URL), data=data)
        return res.ok

    def send_audio(self, chat_id, file):
        data = {
            'chat_id': chat_id,
            'audio': file
        }
        files = {
            'file': open(file, 'rb')
        }
        headers = {
            'Content-Type': 'multipart/form-data'
        }
        res = requests.post('{}sendVoice'.format(
            Config.BOT_URL), data=data, headers=headers, files=files)
        return res.ok
