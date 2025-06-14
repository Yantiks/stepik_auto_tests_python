import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.common import NoSuchElementException


def answer_method():
    answer = math.log(int(time.time()))
    return answer

#link = "https://stepik.org/lesson/236895/step/1"
#переписать локаторы с названиями кнопок через текст кнопок
#поправить линки только с айди страницы

@pytest.mark.parametrize('link', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
class TestAuthorization():

    def test_authorization_site(self, browser_3_6, link):
        config_path = Path(__file__).parent.parent / "config.json"

        # чтение кредов из файла
        with open(config_path, 'r') as f:
            config = json.load(f)
        username = config['username']
        password = config['password']

        link_lesson = f"https://stepik.org/lesson/{link}"
        browser_3_6.get(link_lesson)

        # найти и нажать кнопку Войти + ожидания
        locator = By.ID, "ember479"
        enter_button = wait(browser_3_6, 5).until(EC.presence_of_element_located(locator))
        enter_button.click()

        # в попапе ввести имейл и пароль
        locator_email = By.ID, "id_login_email"
        email_field = wait(browser_3_6, 2).until(EC.presence_of_element_located(locator_email))
        email_field.send_keys(username)

        locator_passw = By.ID, "id_login_password"
        email_field = wait(browser_3_6, 5).until(EC.presence_of_element_located(locator_passw))
        email_field.send_keys(password)

        # нажать кнопку Войти и проверить закрытие модального окна
        modal_auth = By.ID, "ember538"
        button_form_locator = By.CSS_SELECTOR, 'button[type = "submit"]'
        button_form = wait(browser_3_6, 5).until(EC.element_to_be_clickable(button_form_locator))
        button_form.click()
        wait(browser_3_6, 5).until(EC.invisibility_of_element_located(modal_auth))


        #если уже решено
        try:
            button_again = By.CSS_SELECTOR, ".again-btn.white"
            again_button = browser_3_6.find_element(*button_again)
            if again_button.text == "Решить снова":
                again_button.click()
            print("Кнопка найдена и нажата")
        except NoSuchElementException:
            print("Кнопка не найдена, пропускаем")


        answ = answer_method()
        text_field = By.TAG_NAME, "textarea"
        text_field_answer = wait(browser_3_6, 5).until(EC.presence_of_element_located(text_field))
        text_field_answer.click()
        text_field_answer.send_keys(answ)

        button_send_loc = By.CSS_SELECTOR, '.submit-submission'
        button_send = wait(browser_3_6, 5).until(EC.element_to_be_clickable(button_send_loc))
        button_send.click()

        loc_result = By.CLASS_NAME, 'smart-hints__hint'
        result_field = wait(browser_3_6, 5).until(EC.presence_of_element_located(loc_result))
        result = result_field.text
        exp_res = "Correct!"
        print(result)

        assert result == exp_res, f"Текущий ответ: {result}"