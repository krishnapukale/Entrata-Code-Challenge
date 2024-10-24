import os
import re
import shutil

import pytest
from Config import global_var

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser")
    parser.addoption("--headless", default="false", help="headless")   

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def headless(request):
    return request.config.getoption("--headless")