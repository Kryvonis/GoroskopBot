import os
from xml.etree import ElementTree as ET

from gtts import gTTS
from telegram import Bot

from app.core.telegram.telegram_cmd import TelegramCommand
from app.settings import Config


class ShowWeekSoundCommand(TelegramCommand):
    def execute(self):
        bot = Bot(Config.BOT_TOKEN)

        root = ET.parse(
            f'{Config.BASE_PATH}/app/storage/weekly.xml')
        horoscope = root.find('gemini/common')

        if horoscope.text:
            text = ' '.join(horoscope.text.split())

            sound_name = f'{Config.BASE_PATH}/app/storage/{self.user_name}_w.mp3'
            if os.path.exists(sound_name):
                os.remove(sound_name)

            tts = gTTS(text=text, lang='ru')
            tts.save(sound_name)
            bot.send_voice(self.chat_id, open(sound_name, 'rb'))
            return True
        self.send_message(self.chat_id, 'Sorry something goes wrong')
