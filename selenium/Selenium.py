'''
Created on Sep 11, 2024

@author: admin
type: chrome://version on your chrome browser to get the version
        Google Chrome	137.0.7151.120 (Official Build) (64-bit) (cohort: Stable) 
        Revision	707269b903b9d66dcfc06ea5101eec3cf7cdb12b-refs/branch-heads/7151@{#2357}
        OS	Windows 10 Version 22H2 (Build 19045.5965)
File explorer:
        C:\chromedriver-win64_128p0p6613p137
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb
import constants  as const # Assuming constants.py is in the same directory

class MySelenium:
    """A class to demonstrate basic Selenium operations with Chrome WebDriver."""
    def __init__(self):
        """Initialize the MySelenium class."""
        self.driver = None

    def start(self):
        """Start the Chrome WebDriver."""
        self.driver = webdriver.Chrome()
        return self.driver

    def example01(self):
        """Example of using Selenium to interact with a web form."""
        # driver = webdriver.Chrome()
        driver = self.start()
        driver.get(const.SELENIUM_URL)
        # Implicit wait for elements to load
        driver.implicitly_wait(8)
        #title = driver.title
        #pdb.set_trace()  # Set a breakpoint here to inspect the state
        text_box = driver.find_element(by=By.NAME, value="my-text")
        text_box.send_keys("Selenium")

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        submit_button.click()

        message = driver.find_element(by=By.ID, value="message")
        text = message.text
        print(f"\n\n{text}\n\n")
        # Explicit wait for the message to be present
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "Received!"))

        input("Press any key..")
        self.stop()

    def stop(self):
        if self.driver:
            self.driver.quit()

class Booking(webdriver.Chrome):
    """A class to demonstrate a custom WebDriver for booking operations."""
    def __init__(self, teardown=True, *args, **kwargs):
        """Initialize the Booking class."""
        self.teardown = teardown
        super(Booking, self).__init__(*args, **kwargs)
        self.implicitly_wait(10)  # Set an implicit wait for elements to load
        self.maximize_window()  # Optional: Maximize the browser window for better visibility

    def land_first_page(self):
        """Navigate to the Booking.com homepage."""
        #self.start()
        self.get(const.BASE_URL)
        # Add more booking-related operations here
        #input("Press any key to continue...")
        #self.quit()
    
    def change_currency(self, currency: str = None):
        """Change the currency on the Booking.com page."""
        try:
            wait = WebDriverWait(self, 20)  # Increase wait time
            currency_element = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='header-currency-picker-trigger']"))
            )
            currency_element.click()
            try:
                with open("debug_log.txt", "w", encoding="utf-8") as log_file:
                    log_file.write(self.page_source)
            except Exception as eee:
                print(f"Error writing to debug_log.txt: {eee}")

            if currency:
                # Updated XPATH to match the actual button structure in the modal
                xpath = f"//button[@data-testid='selection-item' and .//div[contains(@class, 'CurrencyPicker_currency') and text()='{currency}']]"
                currency_option = wait.until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                currency_option.click()
        except Exception as e:
            raise Exception("Currency button not found, not clickable, or currency option missing on the page.") from e

    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        """Ensure the WebDriver is closed properly."""
        if self.teardown:
            if self.driver:
                self.driver.quit()
        print(f"\n\n Exiting Booking class and closing WebDriver. \n\n")
        #self.quit()

    def select_place_to_go(self, place: str = None):
        """Select a place to go on the Booking.com page."""
        import time
        try:
            wait = WebDriverWait(self, 20)
            place_to_go_element = wait.until(
                EC.element_to_be_clickable((By.NAME, "ss"))
            )
            place_to_go_element.clear()
            place_to_go_element.send_keys(place)
            time.sleep(3)  # Give time for suggestions to load
            try:
                first_result = wait.until(
                    EC.element_to_be_clickable((By.ID, "autocomplete-result-0"))
                )
            except Exception:
                # Try a more flexible CSS selector if ID fails
                first_result = wait.until(
                    #EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-i='0']"))
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "li[tabindex='-1']"))
                )
            first_result.click()
            input("\n\nPress any key to continue...\n\n")
        except Exception as e:
            #print(self.page_source[:2000])  # Print part of the page source for debugging
            raise Exception("Place to go input not found, not clickable, or no autocomplete result.") from e
        
#object01 = MySelenium()
#object01.example01()
object02 = Booking()
object02.land_first_page()
#object02.change_currency("GBP")
object02.select_place_to_go("New York")
object02.quit()

