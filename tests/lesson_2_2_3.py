from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("John")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Doe")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("<EMAIL>")

    file_element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_element.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    print(link)
    time.sleep(10)
    browser.quit()