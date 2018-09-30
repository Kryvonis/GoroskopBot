import json
from xml.etree import ElementTree as ET
from app.core.telegram.telegram_cmd import TelegramCommand
from app.settings import Config


class ShowCommand(TelegramCommand):
    def execute(self):
        root = ET.parse(
            f'{Config.BASE_PATH}/app/storage/daily.xml')
        zs = self.user['zodiac_sign']
        if not zs:
            self.send_message(
                self.chat_id,
                f"{self.user_name}, your day advice is\n"
                f"**Your zodiac sign not setted**"
            )
            return

        horoscope = root.find(f'{zs.value}/today')
        if horoscope.text:
            text = ' '.join(horoscope.text.split())

        self.send_message(
            self.chat_id,
            f"{self.user_name}, your day advice is\n"
            f"**{text}**"
        )
