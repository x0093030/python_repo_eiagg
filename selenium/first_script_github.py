'''
Created on Sep 13, 2024
https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L4
@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
input("Press any key + ENTER ")

text_box.send_keys("Selenium")
submit_button.click()
input("Press any key + ENTER ")

message = driver.find_element(by=By.ID, value="message")
text = message.text
input("Press any key + ENTER ")

driver.quit()