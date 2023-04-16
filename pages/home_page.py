from constants.home_page import HomePageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = HomePageConst

    @log_wrapper
    def verify_home_page_opened(self):
        """Verify Home page opened"""
        assert self.compare_element_text(xpath=self.const.HOME_PAGE_XPATH, text= self.const.HOME_PAGE_TEXT)

    @log_wrapper
    def navigate_to_katalon_courses_page(self):
        """Navigate to katalon courses page"""
        self.click(xpath=self.const.KATALON_COURSES)
        self.click(xpath=self.const.TABLE_MENU)
        self.click(xpath=self.const.WHY_KATALON_XPATH)
        self.click(xpath=self.const.TO_WHY_KATALON_PAGE)

        from pages.katalon_page import KatalonPage
        return KatalonPage(self.driver)




