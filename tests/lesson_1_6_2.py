import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link_site = "http://suninjuly.github.io/find_link_text"

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = webdriver.Chrome()
browser.get(link_site)

link = browser.find_element(By.LINK_TEXT, link_text)
link.click()

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
browser.quit()

