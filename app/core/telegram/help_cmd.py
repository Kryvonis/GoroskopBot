from app.core.telegram.telegram_cmd import TelegramCommand


class HelpCommand(TelegramCommand):
    def execute(self):
        msg = f"This is an Goroskop bot. You can send me " \
              f"your " \
              f"zodiak, and after that I'll send your a weather in your" \
              f" place.\n" \
              f"Also I have an daily advice for you, so just send a /show" \
              f" command to see what I have for you."
        return self.send_message(self.chat_id, msg)


class StartCommand(TelegramCommand):
    def execute(self):
        msg = f"""
        Hello dear {self.user_name} 
        This is an advice bot. You can send me your 
        location, and after that I'll send your a weather in your place.\n
        Also I have an daily advice for you, so just send a /show
        command to see what I have for you.\n
        You always can get help about bot commands and other info.
        Just send /help command for it."""
        return self.send_message(self.chat_id, msg)
