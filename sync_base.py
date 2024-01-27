import pyrogram
import config

import model.base

session = model.base.session
app = pyrogram.Client(config.name, config.api_id, config.api_hash)


def start_parse_leo(limit):
    with app:
        chat_id = 'leomatchbot'
        messages = app.get_chat_history(chat_id, limit=limit)

        # Обработка полученных сообщений
        for message in messages:
            if not message.caption is None:
                add_to_base(caption=message.caption)


def add_to_base(caption):
    if not session.query(model.base.Users).filter_by(caption=caption).first():
        print(caption)
        new_data = model.base.Users(caption=caption)
        session.add(new_data)
        session.commit()


start_parse_leo(1000000)
