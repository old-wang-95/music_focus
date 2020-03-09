import gc
import time

from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException


def get_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--lang=zh-CN")
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference("intl.accept_languages", "zh-CN")
    driver = webdriver.Firefox(firefox_profile=profile, options=options, log_path='log/firefox.log')
    return driver


firefox_driver = get_driver()


def find_elements_in_page(url, css_selector, driver=firefox_driver, wait_time=5, retry_time=3):
    while retry_time:
        try:
            driver.get(url)
            break
        except InvalidSessionIdException as e:
            driver.quit()
            del driver, firefox_driver
            gc.collect()
            driver = get_driver()
            retry_time -= 1
    time.sleep(wait_time)
    driver.set_window_size(
        driver.execute_script('return document.body.parentNode.scrollWidth'),
        driver.execute_script('return document.body.parentNode.scrollHeight'),
    )
    for element in driver.find_elements_by_css_selector(css_selector):
        yield element


def screenshot(element, image_path):
    element.screenshot(image_path)
