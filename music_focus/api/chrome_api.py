import sys
import time

from selenium import webdriver


def find_elements_in_page(url, css_selector, wait_time=5):
    if sys.platform.startswith('darwin'):
        driver_file = 'music_focus/drivers/chromedriver_mac64'
    elif sys.platform.startswith('linux'):
        driver_file = 'music_focus/drivers/chromedriver_linux64'
    else:
        raise SystemError('can not recognize sys.platform: {}, must be darwin or linux!'.format(sys.platform))
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(driver_file, options=options)

    driver.get(url)
    time.sleep(wait_time)
    driver.set_window_size(
        driver.execute_script('return document.body.parentNode.scrollWidth'),
        driver.execute_script('return document.body.parentNode.scrollHeight'),
    )
    for element in driver.find_elements_by_css_selector(css_selector):
        yield element

    driver.quit()


def screenshot(element, filename, dirname='.'):
    element.screenshot('{}/{}'.format(dirname, filename))
