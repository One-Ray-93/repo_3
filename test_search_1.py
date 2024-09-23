from selene import browser, be, have


def test_google_search_1(setup_browser):
    browser.element('[name="q"]').should(be.visible).should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="botstuff"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_search_google_2_invalid(setup_browser, check_results):
    browser.element('[name="q"]').should(be.visible).should(be.blank).type('@@@98342g+3y89438+25b').press_enter()
    browser.element('[id="botstuff"]').should(have.text('ничего не найдено'))
