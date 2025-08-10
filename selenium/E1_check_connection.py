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

"""
if (.\venv\Scripts\Activate.ps1) FAILS
    error: Activate.ps1 cannot be loaded because running scripts is disabled on this system.
    You may need to change the execution policy to allow scripts to run. You can do this by running the following command in PowerShell as an administrator:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
else
    python -m venv venv
    pip install selenium
    pip install webdriver-manager
    python E1_check_connection.py
"""