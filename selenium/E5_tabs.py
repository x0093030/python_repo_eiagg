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
    
    def test_change_tab(self):
        self.setUp()
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://stackoverflow.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
        
        self.teardown()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'unittest.TestCase']
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)
    unittest.main()