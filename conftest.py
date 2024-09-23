import pytest
from selene import browser

@pytest.fixture
def setup_browser(browser_2_open):
    browser.config.window_width = 800
    browser.config.window_height = 600

    yield
    browser.quit()


@pytest.fixture
def browser_2_open():
    browser.open('https://www.google.co.uk/')

@pytest.fixture
def check_results():
    browser.open('https://www.google.co.uk/')
    yield
    print("Не найдено результатов поиска")
    browser.quit()