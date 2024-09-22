import pytest
from selene import browser, be, have

def test_google_search_invalid(browser_open, setup_browser, check_results):
    browser.element('[name="q"]').should(be.visible).should(be.blank).type('NTGSETNWZ3RTMSUSR5YM').press_enter()
    browser.element('[id="search"]').should(have.text('Your search - NTGSETNWZ3RTMSUSR5YM - did not match any documents.'))