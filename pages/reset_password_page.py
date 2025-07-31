import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage): 
    def check_password_input_activate_by_click(self):
        self.click_to_element(ResetPasswordLocators.SVG_SHOW_HIDE_PASSWORD)
        element = self.find_visible_element(ResetPasswordLocators.INPUT_PASSWORD_ACTIVE)
        if element:
            return True
        return False
    
    @allure.step('Проверка, что на странице есть поле для ввода кода подтверждения')
    def _verify_page_loaded(self):
        confirm_label = self.find_visible_element(ResetPasswordLocators.LABEL_CONFIRMATION_CODE)
        return all([confirm_label])