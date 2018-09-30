from flask import request
from flask.views import MethodView

from app.core.telegram import *


command_dict = {
    '/show': ShowCommand,
    '/show_sound': ShowSoundCommand,
    '/show_w': ShowWeekCommand,
    '/show_w_sound': ShowWeekSoundCommand,
    '/help': HelpCommand,
    '/start': StartCommand,
    '/set': SetCommand,

}


class IndexView(MethodView):
    def get(self):
        return 'Hello', 200

    def post(self):
        r = request.get_json()
        if r:
            message = r.get('message')
            if message:
                entities = message.get('entities')
                if entities:
                    command = message['text'][:entities[0]['length']]
                    if command in command_dict.keys():
                        cmd = command_dict[command](message)
                        cmd.execute()
        return 'OK', 200
