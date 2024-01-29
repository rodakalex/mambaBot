import vk
import time

api = vk.API(
    # Токен получается только через авторизованные приложения. Нужно разрешить доступ, например к Марусе, а затем
    # скопировать её в строку ниже
    # https://vkhost.github.io/
    access_token='',
    v='5.199')
user_id = '-91050183'


def send_reaction(reaction):
    try:
        api.messages.send(user_id=user_id, message=reaction, random_id=0)
    except vk.exceptions.VkAPIError as err:
        captcha_key = input(f"Пора ввести каптчу: {err.captcha_img}\n")
        api.messages.send(user_id=user_id, message=reaction, random_id=0, captcha_key=captcha_key, captcha_sid=err.captcha_sid)


def send_messages(text):
    time.sleep(1)

    count_likes = 0
    while count_likes != 50:
        time.sleep(10)
        last_message = api.messages.getHistory(count=1, user_id=user_id)
        if len(last_message['items'][0]['text']) > 100:
            count_likes += 1
            send_reaction(1)
        else:
            send_reaction(3)


def run():
    send_messages('1')


if __name__ == '__main__':
    run()
