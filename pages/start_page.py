from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def navigate_to_home_page(self):
        """Navigate to Home page"""
        self.click(xpath=self.const.HOME_XPATH)

        from pages.home_page import HomePage
        return HomePage(self.driver)

    @log_wrapper
    def navigate_to_git_page(self):
        """Navigate to katalon courses page"""
        self.click(xpath=self.const.TUTORIALS_MENU_XPATH)
        self.click(xpath=self.const.DEVOPSTOOLS_XPATH)
        self.click(xpath=self.const.GIT_XPATH)

        from pages.git_page import GitPage
        return GitPage(self.driver)

