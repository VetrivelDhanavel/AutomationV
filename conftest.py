import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope='session')
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()

@pytest.fixture(scope='function')
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)

