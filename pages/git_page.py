from constants.git_page import GitPageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper

class GitPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = GitPageConst

    @log_wrapper
    def verify_git_page_opened(self):
        """Verify Git page opened"""
        assert self.compare_element_text(xpath=self.const.GIT_PAGE_XPATH, text= self.const.GIT_PAGE_TEXT)
