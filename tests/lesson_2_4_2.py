from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id = 'input_value']")
    x = x_element.text
    y = calc(x)
    print(y)

    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()





finally:
    time.sleep(10)
    browser.quit()