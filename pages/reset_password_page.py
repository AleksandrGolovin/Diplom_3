import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):
    
    @allure.step('Статус проверки, что при клике на кнопку отображения пароля окно ввода становится активным')
    def is_password_input_activate_by_click(self):
        self.click_to_element(ResetPasswordLocators.SVG_SHOW_HIDE_PASSWORD)
        element = self.find_visible_element(ResetPasswordLocators.INPUT_PASSWORD_ACTIVE)
        if element:
            return True
        return False
    
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(ResetPasswordLocators.LABEL_CONFIRMATION_CODE)
        ]
        return all(conditions)