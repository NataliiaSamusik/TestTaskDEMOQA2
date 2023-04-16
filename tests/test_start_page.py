"""Tests related to start page"""
import logging
import pytest
from conftest import start_page
from constants.base import BaseConstants

@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestStartPage:
    """Stores tests for start page """

    def test_home_page_opens(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Click on HOME menu tab
            - Verify Start page
        """
        # Click on HOME menu tab
        home_page = start_page.navigate_to_home_page()
        # Verify Home page opens
        home_page.verify_home_page_opened()

    def test_git_page_opens(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Click on TUTORIALS menu tab
            - Select DeVops Tools > Git
            - Verify Git page
        """
        # Click on TUTORIALS menu tab
        # Select DeVops Tools > Git
        git_page = start_page.navigate_to_git_page()
        # Verify Git page
        git_page.verify_git_page_opened()



