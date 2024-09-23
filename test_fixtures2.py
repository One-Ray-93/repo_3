import pytest

@pytest.fixture
def browser():
    pass

@pytest.fixture
def login_page(browser):
    pass
    yield
    print ("Логин")

@pytest.fixture
def user():
    return "username", "password"

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
