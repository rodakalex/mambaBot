import time
import pyrogram
import config
from pyrogram import filters

import model.base

session = model.base.session
app = pyrogram.Client(config.name, config.api_id, config.api_hash)


def send_messages(text):
    time.sleep(1)
    app.send_message(chat_id='leomatchbot', text=text)


@app.on_message(filters.private)
def handle_message(client, message):
    if message.caption is None:
        time.sleep(10)
    else:
        if len(message.caption) < 100:
            time.sleep(1)
            send_messages('3')
        elif not session.query(model.base.Users).filter_by(caption=message.caption).first():
            time.sleep(1)
            send_messages('2')
            send_messages('Ты классная :3')
            new_data = model.base.Users(caption=message.caption)
            session.add(new_data)
            session.commit()


if __name__ == '__main__':
    print("The program is running")
    app.run()
