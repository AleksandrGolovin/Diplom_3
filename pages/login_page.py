import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import URL


class LoginPage(BasePage):
    BASE_URL = URL.LOGIN_PAGE
    
    @allure.step('Авторизация пользователя по email и password')
    def auth(self, email, password):
        self.set_text_to_element(LoginPageLocators.INPUT_EMAIL, email)
        self.set_text_to_element(LoginPageLocators.INPUT_PASSWORD, password)
        return self.navigate_to_main_page()
    
    @allure.step('Переход на страницу восстановления пароля по клику на ссылку восстановления пароля')
    def navigate_to_forgot_password_page(self):
        self.click_to_element(LoginPageLocators.LINK_RESTORE_PASSWORD)
        
        from pages.forgot_password_page import ForgotPasswordPage
        destination_page = ForgotPasswordPage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError

    @allure.step('Переход на главную страницу по клику на кнопку входа по логину-паролю')
    def navigate_to_main_page(self):
        self.click_to_element(LoginPageLocators.BUTTON_LOGIN)
        
        from pages.main_page import MainPage
        destination_page = MainPage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError
    
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(LoginPageLocators.H2_LOGIN_TITLE)
        ]
        return all(conditions)