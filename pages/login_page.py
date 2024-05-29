from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = page.get_by_placeholder("youremail@email.com")
        self.password_input = page.get_by_placeholder("password")
        self.login_button = page.get_by_role("button", name="Login")
        self.username_display = page.get_by_text("vetrivel").nth(1)
        self.logout_link = page.get_by_text("Log Out")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.username_display.click()
        self.logout_link.click()
