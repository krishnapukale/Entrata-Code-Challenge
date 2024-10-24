from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Pages.Home.home_page_loc import HomePageLocators


class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self.homePageLocators = HomePageLocators


    def open_page(self, url):
        self.driver.get(url)


    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            assert False, f"Element not found:{locator}"
        

    
    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except NoSuchElementException:
            assert False, f"Element not found:{locator}"


    def click(self, by_locator: object) -> object:
        self.wait.until((EC.visibility_of_element_located(by_locator)))
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    

    def Wait_For_Element_Clickable(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            return element
        except Exception as e:
            print(str(e))