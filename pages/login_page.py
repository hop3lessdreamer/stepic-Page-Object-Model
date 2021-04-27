from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', 'Вы не на странице авторизации'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), 'Нет формы логина'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presented(*LoginPageLocators.REGISTRATION_FORM), 'Нет формы регистрации'

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        reg_password.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        reg_btn.click()