from constants.katalon_page import KatalonPageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper


class KatalonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = KatalonPageConst

    @log_wrapper
    def verify_katalon_page_opened(self):
        """Verify Katalon page opened"""
        assert self.compare_element_text(xpath=self.const.WHY_KATALON_OPENS_XPATH, text= self.const.WHY_KATALON_OPENS_TEXT)
