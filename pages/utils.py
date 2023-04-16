import datetime
import logging
import string
from time import sleep
from selenium import webdriver
from constants.base import BaseConstants


def wait_until_ok(timeout=5, period=0.25):
    """Retires function until ok (or 5 seconds)"""
    log = logging.getLogger("[WaitUntilOk]")
    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    log.warning(f"Catching: {err}")
                    if datetime.datetime.now() > end_time:
                        raise err
                    sleep(period)
        return wrapper
    return decorator
def log_wrapper(func):
    """Add logs for method based on the docstring"""
    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        # log.info(f"{func.__doc__}; Args: {args}; Kwargs: {kwargs}")
        log.info(func.__doc__)
        return result
    return wrapper
def create_driver(browser):
    """Create driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        driver = webdriver.Chrome(executable_path=BaseConstants.CHROME_DRIVER_PATH)
    elif browser == BaseConstants.FIREFOX:
        driver = webdriver.Firefox(executable_path=BaseConstants.FIREFOX_DRIVER_PATH)
    else:
        raise ValueError(f"Unknown browser name: {browser}")
    driver.implicitly_wait(1)
    driver.get(BaseConstants.URL)
    return driver