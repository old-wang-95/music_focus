import time

from selenium import webdriver


def find_elements_in_page(url, css_selector, wait_time=5):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)

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
