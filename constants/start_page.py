class StartPageConst:
    """Stores constants related to start page"""
    HOME_XPATH = './/a[@href="/"]'
    TUTORIALS_MENU_XPATH = './/a[@class="navbar__tutorial-menu"]'
    DEVOPSTOOLS_XPATH = './/div[@class="first-generation"]//ul[.//li[.//span[contains(text(),"DevOps Tools")]]]'
    GIT_XPATH = './/div[@class="second-generation"]//ul[.//li[.//span[contains(text(),"Git")]]]'
