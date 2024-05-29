from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.register_link = page.get_by_text("Register")
        self.name_input = page.get_by_placeholder("Name")
        self.email_input = page.get_by_placeholder("youremail@email.com")
        self.phone_input = page.locator(".PhoneInput")
        self.phone_number_input = page.get_by_placeholder("Enter phone number")
        self.password_input = page.get_by_placeholder("password")
        self.eye_icon = page.get_by_role("img", name="eye icon")
        self.register_button = page.get_by_role("button", name="Register")

    def register(self, name, email, phone, password):
        self.register_link.click()
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.phone_input.click()
        self.phone_number_input.fill(phone)
        self.password_input.fill(password)
        self.eye_icon.click()
        self.register_button.click()
