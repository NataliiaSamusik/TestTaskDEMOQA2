class HomePageConst:
    """Stores constants related to home page"""
    HOME_PAGE_XPATH = './/div[@class="new-training__heading"]'
    HOME_PAGE_TEXT = 'Selenium Online Trainings'

    KATALON_COURSES = './/a[@href="/katalon-studio-tutorial"]'
    TABLE_MENU = './/span[@class="fs-14 lh-17 font-weight-bold"]'
    WHY_KATALON_XPATH = './/div[@class="toc--menu active"]//ul[.//li[.//span[contains(text(),"Why Katalon Studio?")]]]'
    TO_WHY_KATALON_PAGE = './/a[@href="/katalon-studio/makes-katalon-studio-powerful-selenium-based-frameworks/"]'