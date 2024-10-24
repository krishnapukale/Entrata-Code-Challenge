import pytest
from TestCases.basetest import BaseTest


class TestHomePage(BaseTest):

    "This Test is to Navigate to pages on Home Screen footer"
    def test_navigate_homepages(self,load_pages):
        self.homepage.navigate_to_pages()

    "Thi Test is to Fill out the form from Schedule Your Demo button"
    def test_watch_demo_form(self,load_pages):
        self.homepage.fill_demo_form()

    "This Test is to Fill out the form from home page"
    def test_form_home_page(self,load_pages):
        self.homepage.fill_form_home_page()

    "This Test is to navigate to different banner pages"
    def test_navigate_pages_banner(self,load_pages):
        self.homepage.navigate_pages_banner()