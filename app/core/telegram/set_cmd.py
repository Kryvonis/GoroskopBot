from app.core.telegram.telegram_cmd import TelegramCommand

from sqlalchemy import select

from app import db_engine
from app.core.abstract_command import AbstractCommand
from app.models.models import user


class SetCommand(TelegramCommand):
    ZODIAC_SIGNS = ['aries', 'taurus', 'gemini', 'cancer',
                    'leo', 'virgo', 'libra', 'scorpio',
                    'sagittarius', 'capricorn', 'aquarius', 'pisces'
                    ]

    def execute(self):
        if self.text not in self.ZODIAC_SIGNS:
            return self.send_message(self.chat_id, 'this signt not founded')
        with db_engine.connect() as conn:
                conn.execute(
                    user.update().values(
                        zodiac_sign=self.text,
                    )
                )
                res = conn.execute(select(user.c).where(
                    user.c.telegram_id == self.user_id)).fetchone()
        self.user = dict(res)
        msg = f"""
        Hello dear {self.user_name} 
        This is an Goroskop bot. 
        You can register your zodiac sign, and after that send /show command
        I'll be able to send your a horoscope in your place.\n
        Also I have an weekly horoscope for you, so just send a /show_weekly
        command to see what I have for you.\n
        You always can get help about bot commands and other info.
        Just send /help command for it."""
        return self.send_message(self.chat_id, msg)
