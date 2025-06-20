'''
Created on Sep 12, 2024

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://gmail.com")

user = driver.find_element(by=By.ID, value="identifierId")
user.send_keys("pvdtorre888@gmail.com")
user.send_keys(Keys.ENTER)
time.sleep(3)

passw = driver.find_element(by=By.NAME, value="password")
passw.send_keys("1234")
passw.send_keys(Keys.ENTER)

input("Press any key..")
driver.close()
