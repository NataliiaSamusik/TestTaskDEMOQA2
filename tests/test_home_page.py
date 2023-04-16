"""Tests related to home page"""
import logging
import pytest
from conftest import start_page
from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestHomePage:
    """Stores tests for home page """

    def test_Katalon_page_opens(self, start_page, home_page):
        """
        - Pre-conditions:
            - Open start page
            - Click on HOME menu tab
        - Steps:
            - Click on Katalon icon
            - Click on  Table of Contents to open drop down menu
            - Click on Why Katalon Studio? > Why Katalon Studio is powerful than other Selenium based Frameworks?
            - Verify Katalon page
        """
        # Click on Katalon icon
        # Click on  Table of Contents to open drop down menu
        # Click on Why Katalon Studio? > Why Katalon Studio is powerful than other Selenium based Frameworks?
        katalon_page = home_page.navigate_to_katalon_courses_page()
        # Verify Katalon page
        katalon_page.verify_katalon_page_opened()

