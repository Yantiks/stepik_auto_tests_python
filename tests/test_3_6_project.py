import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


link = "https://stepik.org/lesson/236895/step/1"

class TestAuthorization():

    def test_authorization_site(self, browser_3_6):
        # чтение кредов из файла
        with open('config.json', 'r') as f:
            config = json.load(f)
        username = config['username']
        password = config['password']

        browser_3_6.get(link)
        # найти и нажать кнопку Войти + ожидания

        # в попапе ввести имейл и пароль

        # нажать кнопку Войти
        #browser_3_6find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")