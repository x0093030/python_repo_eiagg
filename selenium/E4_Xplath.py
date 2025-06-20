'''
Created on Sep 20, 2024

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        #close browser window
        #self.driver.close() 
        #close browser window + all related browser in 
        self.driver.quit()

    def test_find_xpath(self):
        self.setUp()
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        self.assertIn("Google", driver.title)

        #Xpath es una structura de objetos
        #Xpath puede ser relativo o absoluto
        relative_path = "//*[@id='APjFqb']"
        absolute_path = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"
        find_xpath_= driver.find_element(by=By.XPATH, value=absolute_path)
        #find_xpath_= driver.find_element(by=By.XPATH, value="//*[@id='APjFqb']")        
        time.sleep(3)
        find_xpath_.send_keys("selenium", Keys.ARROW_DOWN)
        #find_xpath_.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "Element doesn't found!" not in driver.page_source
        self.teardown()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'unittest.TestCase']
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    unittest.main()