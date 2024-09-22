import pytest
from selene import browser, be, have

def test_google_search_invalid(browser_open, setup_browser, check_results):
    browser.element('[id="text"]').should(be.visible).should(be.blank).type('@@@').press_enter()
    browser.element('[id="search-result"]').should(have.text('Ничего не нашли'))