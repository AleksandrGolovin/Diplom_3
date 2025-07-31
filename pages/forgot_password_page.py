import allure
from pages.base_page import BasePage
from pages.reset_password_page import ResetPasswordPage
from locators.forgot_password_page_locator import ForgotPasswordPageLocators
from helpers import generate_unique_email
from data import URL


class ForgotPasswordPage(BasePage):
    def open_page(self):
        self.go_to_url(URL.FORGOT_PASSWORD_PAGE)
    
    @allure.step('Клик на вопрос')
    def enter_email(self, email=None):
        email = email or generate_unique_email()
        self.set_text_to_element(ForgotPasswordPageLocators.INPUT_EMAIL, email)
        
    def submit_restore(self):
        self.click_to_element(ForgotPasswordPageLocators.BUTTON_SUBMIT_RESTORE)
        return ResetPasswordPage(self.driver)
    
    def check_forgot_password_page(self):
        h2_password_restoring = self.find_element_with_wait(ForgotPasswordPageLocators.H2_PASSWORD_RESTORING)
        button_sumbit_restore = self.find_element_with_wait(ForgotPasswordPageLocators.BUTTON_SUBMIT_RESTORE)
        return all([h2_password_restoring, button_sumbit_restore])