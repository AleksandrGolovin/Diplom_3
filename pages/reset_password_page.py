import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators
from data import URL


class ResetPasswordPage(BasePage):
    def open_page(self):
        self.go_to_url(URL.RESET_PASSWORD_PAGE)
    
    def check_password_input_activate_by_click(self):
        self.click_to_element(ResetPasswordLocators.SVG_SHOW_HIDE_PASSWORD)
        element = self.find_element_with_wait(ResetPasswordLocators.INPUT_PASSWORD_ACTIVE)
        if element:
            return True
        return False
    
    @allure.step('Проверка, что на странице есть поле для ввода кода подтверждения')
    def check_reset_password_page(self):
        if self.find_element_with_wait(ResetPasswordLocators.LABEL_CONFIRMATION_CODE):
            return True
        return False