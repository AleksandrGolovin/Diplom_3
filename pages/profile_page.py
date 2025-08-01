import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
      
    @allure.step('Проверка, что на странице есть заголовок входа')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(ProfilePageLocators.TEXT_PROFILE_HINT)
        ]
        return all(conditions)