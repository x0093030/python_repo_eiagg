'''
Created on Sep 24, 2024

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        #close browser window
        #self.driver.close() 
        #close browser window + all related browser in 
        self.driver.quit()
        
    def test_explicit_wait(self):
        self.setUp()
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.NAME, "q")))
        finally:
            print(f"Bye ..{element}")  
        self.teardown()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'unittest.TestCase']
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)
    unittest.main()