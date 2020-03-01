import time

from selenium import webdriver


def find_elements_in_page(url, css_selector, wait_time=5):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--lang=zh-CN")
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference("intl.accept_languages", "zh-CN")
    driver = webdriver.Firefox(firefox_profile=profile, options=options)

    driver.get(url)
    time.sleep(wait_time)
    driver.set_window_size(
        driver.execute_script('return document.body.parentNode.scrollWidth'),
        driver.execute_script('return document.body.parentNode.scrollHeight'),
    )
    for element in driver.find_elements_by_css_selector(css_selector):
        yield element

    driver.quit()


def screenshot(element, image_path):
    element.screenshot(image_path)
