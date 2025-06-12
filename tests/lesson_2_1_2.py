from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.click()
    answer_field.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()