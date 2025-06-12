from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_sum(x, y):
    return x + y

try:
    link = "https://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num1_text = num1.text
    num1_int = int(num1_text)
    num2 = browser.find_element(By.ID, "num2")
    num2_text = num2.text
    num2_int = int(num2_text)

    sum12 = get_sum(num1_int, num2_int)
    sum12_int = str(sum12)

    dropdown_list = browser.find_element(By.ID, "dropdown")
    dropdown_list.click()

    answer = browser.find_element(By.CSS_SELECTOR, f"[value='{sum12_int}']")
    answer.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")

finally:
    time.sleep(10)
    browser.quit()