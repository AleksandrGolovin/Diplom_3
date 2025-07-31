import allure
from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
from locators.login_page_locators import LoginPageLocators
from data import URL


class LoginPage(BasePage):
    def open(self):
        self.go_to_url(URL.LOGIN_PAGE)
        return self
    
    @allure.step('Переход на страницу восстановления пароля')
    def navigate_to_forgot_password_page(self) -> ForgotPasswordPage:
        self.click_to_element(LoginPageLocators.LINK_RESTORE_PASSWORD)
        forgot_password_page = ForgotPasswordPage(self.driver)
        if forgot_password_page.is_page_loaded():
            return forgot_password_page
        raise AssertionError