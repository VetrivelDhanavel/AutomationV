from playwright.sync_api import Playwright, sync_playwright
from pages.registration_page import RegistrationPage

from pages.login_page import LoginPage


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Registration
    registration_page = RegistrationPage(page)
    page.goto("https://tracker.vmmaps.com/login")
    registration_page.register("vetrivel", "vetriveld35@gmail.com", "9655728870", "Vetri@123")

    # Login
    login_page = LoginPage(page)
    login_page.login("vetriveld35@gmail.com", "Vetri@123")

    # Logout
    login_page.logout()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
