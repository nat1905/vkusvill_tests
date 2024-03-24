from selenium.webdriver import Chrome

from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
import logging


@pytest.fixture(scope='class')
def selenium():
    options = ChromeOptions()
    logging.debug(f'Prepare browser')

    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1300,1000")
    options.page_load_strategy = 'normal'  # none eager

    browser = Chrome(options=options)
    browser.implicitly_wait(100)  # неявное ожидание
    logging.debug(f'Browser has been started')

    yield browser
    browser.quit()
