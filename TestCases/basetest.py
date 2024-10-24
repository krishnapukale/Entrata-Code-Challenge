import pytest
from Helpermethods.config_parser import ReadProp
from Helpermethods.drivermanager import DriverManager
from Pages.Home.home_page import HomePage
from Pages.Home.home_page_loc import HomePageLocators


class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self,request, ):
        browser = request.config.getoption("--browser")
        headless = request.config.getoption("--headless")

        self.url = "https://www.entrata.com"
            
        self.driver = DriverManager.drivermanager(browser, headless)
        self.driver.maximize_window()
        self.driver.get(self.url)        
        yield self.driver
        self.driver.close()
        self.driver.quit()

    @pytest.fixture()
    def load_pages(self):
        self.homepage = HomePage(self.driver)
        self.homePageLocator = HomePageLocators