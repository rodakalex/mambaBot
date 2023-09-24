import time
import pyrogram
import config


class Leomathcbot:
    def __init__(self):
        self.app = pyrogram.Client(config.name, config.api_id, config.api_hash)
        self.app.start()

    def send_messages(self):
        for i in range(200):
            time.sleep(1)
            self.app.send_message(chat_id='leomatchbot', text='1')

    def __del__(self):
        del self.app


if __name__ == '__main__':
    bot = Leomathcbot()
    bot.send_messages()
