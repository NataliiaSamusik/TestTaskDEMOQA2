import pytest
from pages.start_page import StartPage
from pages.utils import create_driver

@pytest.fixture()
def driver(browser):
    """Creates selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()

@pytest.fixture()
def start_page(driver):
    """Creates start page object"""
    return StartPage(driver)

@pytest.fixture()
def home_page(start_page):
    """Navigate to PRODUCT page"""
    home_page = start_page.navigate_to_home_page()
    return home_page


