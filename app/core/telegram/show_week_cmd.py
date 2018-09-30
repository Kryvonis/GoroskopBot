from xml.etree import ElementTree as ET

from app.core.telegram.telegram_cmd import TelegramCommand
from app.settings import Config


class ShowWeekCommand(TelegramCommand):
    def execute(self):
        root = ET.parse(
            f'{Config.BASE_PATH}/app/storage/weekly.xml')
        horoscope = root.find('gemini/common')
        if horoscope:
            text = ' '.join(horoscope.text.split())
        self.send_message(
            self.chat_id,
            f"{self.user_name}, your day advice is\n"
            f"**{text}**"
        )