from selenium import webdriver

class DriverManager:

    @staticmethod
    def drivermanager(browser, headless):
        if browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            if headless.lower() == 'true':
                options.add_argument('--headless')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-notifications')
            driver = webdriver.Chrome(options=options)
        else:
            raise Exception("Incorrect Browser")
        return driver