import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step('Показать историю заказов')
    def show_orders_history(self):
        self.click_to_element(ProfilePageLocators.LINK_HISTORY)
    
    @allure.step('Показать историю заказов')    
    def is_orders_history_displayed(self):
        self.wait_for_invisibility(ProfilePageLocators.DIV_LOADING)
        if self.find_invisible_element(ProfilePageLocators.DIV_ORDER_HISTORY):
            return True
        return False

    @allure.step('Показать историю заказов')
    def logout(self):
        self.click_to_element(ProfilePageLocators.BUTTON_LOGOUT)
        
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(ProfilePageLocators.TEXT_PROFILE_HINT)
        ]
        return all(conditions)