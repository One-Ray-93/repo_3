import pytest
from selene import browser

@pytest.fixture
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.hold_browser_open = False  # Браузер закрывается после тестов
    browser.config.timeout = 10  # Увеличиваем время ожидания элементов
    yield
    browser.quit()

@pytest.fixture
def browser_open():
    browser.open('https://google.com')

@pytest.fixture
def check_results():
    browser.open('https://google.com')
    yield
    print("Не найдено результатов поиска")
