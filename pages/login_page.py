import allure
from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage
from locators.login_page_locators import LoginPageLocators
from data import URL


class LoginPage(BasePage):
    BASE_URL = URL.LOGIN_PAGE
    
    def auth(self, email, password) -> MainPage:
        self.set_text_to_element(LoginPageLocators.INPUT_EMAIL, email)
        self.set_text_to_element(LoginPageLocators.INPUT_PASSWORD, password)
        return self.navigate_to_main_page()
    
    @allure.step('Переход на страницу восстановления пароля')
    def navigate_to_forgot_password_page(self) -> ForgotPasswordPage:
        self.click_to_element(LoginPageLocators.LINK_RESTORE_PASSWORD)
        
        forgot_password_page = ForgotPasswordPage(self.driver)
        if forgot_password_page.is_page_loaded():
            return forgot_password_page
        raise AssertionError

    @allure.step('Переход на главную страницу')
    def navigate_to_main_page(self) -> MainPage:
        self.click_to_element(LoginPageLocators.BUTTON_LOGIN)
        
        main_page = MainPage(self.driver)
        if main_page.is_page_loaded():
            return main_page
        raise AssertionError
    
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(LoginPageLocators.H2_LOGIN_TITLE)
        ]
        return all(conditions)