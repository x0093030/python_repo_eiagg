'''
Created on Sep 13, 2024

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#from test.leakers import test_selftype


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()

    def testFind(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        #input("Press any key + ENTER ")
        
        element=driver.find_element(by=By.NAME, value="q")
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        input("Press any key + ENTER ")
        
        assert "Element doesn't found!" not in driver.page_source
    
    def teardown(self):
        self.driver.close()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main()