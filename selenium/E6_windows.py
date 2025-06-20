'''
Created on Sep 21, 2024

@author: admin
'''
import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        #close browser window
        #self.driver.close() 
        #close browser window + all related browser in 
        self.driver.quit()
    
    def test_windows(self):
        self.setUp()
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("https://stackoverflow.com")
        time.sleep(3)
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        
        self.teardown()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'unittest.TestCase']
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)
    unittest.main()