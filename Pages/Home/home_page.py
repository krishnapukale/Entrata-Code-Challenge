from Pages.basepage import BasePage
from Pages.Home.home_page_loc import HomePageLocators
from Testdata.testdata import TestData
import time
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_pages(self):
        self.click(self.homePageLocators.btn_cookie_close)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_residentpay)
        self.click(self.homePageLocators.link_residentpay)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_residentportal)
        self.click(self.homePageLocators.link_residentportal)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_EBI)
        self.click(self.homePageLocators.link_EBI)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_RBI)
        self.click(self.homePageLocators.link_RBI)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_SRI)
        self.click(self.homePageLocators.link_SRI)

    def fill_demo_form(self):
        self.click(self.homePageLocators.btn_cookie_close)
        self.Wait_For_Element_Clickable(self.homePageLocators.btn_close_banner)
        self.click(self.homePageLocators.btn_close_banner)
        time.sleep(3)
        self.click(self.homePageLocators.btn_watch_demo)
        self.send_keys(self.homePageLocators.inp_firstname,TestData.first_name)
        self.send_keys(self.homePageLocators.inp_lastname,TestData.last_name)
        self.send_keys(self.homePageLocators.inp_email,TestData.email)
        self.send_keys(self.homePageLocators.inp_company,TestData.company_name)
        self.send_keys(self.homePageLocators.inp_phone,TestData.phone_number)
        self.click(self.homePageLocators.select_units)
        self.Wait_For_Element_Clickable(self.homePageLocators.option_value)
        self.click(self.homePageLocators.option_value)
        assert self.is_displayed(self.homePageLocators.select_units),"No option selected"
        self.send_keys(self.homePageLocators.inp_jobtitle,TestData.job_title)
        time.sleep(2)
        self.click(self.homePageLocators.select_iam)
        assert self.is_displayed(self.homePageLocators.select_iam),"No option selected"
        self.Wait_For_Element_Clickable(self.homePageLocators.option_resident)
        self.click(self.homePageLocators.option_resident)


    def fill_form_home_page(self):
        self.click(self.homePageLocators.btn_cookie_close)
        self.Wait_For_Element_Clickable(self.homePageLocators.btn_close_banner)
        self.click(self.homePageLocators.btn_close_banner)
        time.sleep(3)
        self.send_keys(self.homePageLocators.inp_firstname,TestData.first_name)
        self.send_keys(self.homePageLocators.inp_lastname,TestData.last_name)
        self.send_keys(self.homePageLocators.inp_email,TestData.email)
        self.send_keys(self.homePageLocators.inp_company,TestData.company_name)
        self.send_keys(self.homePageLocators.inp_phone,TestData.phone_number)
        self.click(self.homePageLocators.select_units)
        self.Wait_For_Element_Clickable(self.homePageLocators.option_value)
        self.click(self.homePageLocators.option_value)
        self.send_keys(self.homePageLocators.inp_jobtitle,TestData.job_title)
        time.sleep(2)
        self.click(self.homePageLocators.select_iam)
        self.Wait_For_Element_Clickable(self.homePageLocators.option_resident)
        self.click(self.homePageLocators.option_resident)

    def navigate_pages_banner(self):
        self.click(self.homePageLocators.btn_cookie_close)
        self.Wait_For_Element_Clickable(self.homePageLocators.btn_close_banner)
        self.click(self.homePageLocators.btn_close_banner)
        time.sleep(3)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_property_manage)
        self.click(self.homePageLocators.link_property_manage)
        self.click(self.homePageLocators.link_home)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_marketing)
        self.click(self.homePageLocators.link_marketing)
        self.click(self.homePageLocators.link_home)
        time.sleep(2)
        self.click(self.homePageLocators.link_accounting)
        self.click(self.homePageLocators.link_home)
        self.Wait_For_Element_Clickable(self.homePageLocators.link_utilities)
        self.click(self.homePageLocators.link_utilities)
        