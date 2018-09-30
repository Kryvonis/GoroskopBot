from abc import ABCMeta, abstractmethod


class AbstractCommand(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def send_message(self, chat_id, text):
        pass
