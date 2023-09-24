import config
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pickle


class Mamba:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.girls_id: list = []

    def login(self):
        self.driver.get('https://www.mamba.ru/ru/login')
        element = self.driver.find_element(By.NAME, 'login')
        element.send_keys(config.email)
        element = self.driver.find_element(By.NAME, 'password')
        element.send_keys(config.password)
        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def search(self):
        """
        TODO:
            1. Проверить входит ли найденный ID в список уже существующих
        """
        self.driver.get('https://www.mamba.ru/search/list')

        time.sleep(5)
        elements = self.driver.find_elements(By.XPATH, '//div[@data-name="search-list-item"]/a')

        for i in elements:
            _new_string = i.get_attribute('href')[29:]
            _temp = _new_string.find('/')
            _new_string = _new_string[0:_temp]
            self.girls_id.append(_new_string)

    def save_girls_id(self):
        with open('girls.pickle', 'wb') as handle:
            pickle.dump(self.girls_id, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def send_messages(self):
        """
        TODO:
            1. Записать в список отправленных сообщений
        """

        with open('girls.pickle', 'rb') as handle:
            girls = pickle.load(handle)

        example = 'https://www.mamba.ru/profile/1808470814'
        for girl_id in self.girls_id:
            try:
                self.driver.get(f'https://www.mamba.ru/chats/{girl_id}/contact')
                time.sleep(3)
                element = self.driver.find_element(By.XPATH, '//textarea')
                element.send_keys('Привет :3')
                webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()
            except:
                pass

    def send_likes(self):
        self.driver.get('https://www.mamba.ru/rating')
        time.sleep(2)

        for _ in range(1000):
            time.sleep(1)
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            webdriver.ActionChains(self.driver).send_keys(Keys.RIGHT).perform()

    def exit(self):
        self.driver.close()


if __name__ == '__main__':
    m = Mamba()
    m.login()
    # time.sleep(5)

    # алгоритм отправки сообщений
    # m.search()
    # m.save_girls_id()
    # m.send_messages()

    # алгоритм лайков
    m.send_likes()

    m.exit()
