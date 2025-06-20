'''
Created on Sep 12, 2024

@author: admin
'''
from selenium import webdriver
#driver = webdriver.Chrome(executable_path-r"C:\chromedriver-win64_128p0p6613p137\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
input("Press any key..")
driver.close()
