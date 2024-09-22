import pytest
from selene import browser, be, have

def test_google_search(browser_open, setup_browser):
    browser.element('[name="q"]').should(be.visible).should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))
