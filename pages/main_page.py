import allure
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators
from data import URL


class MainPage(BasePage):
    BASE_URL = URL.MAIN_PAGE
    
    @allure.step('Переход на страницу личного кабинета пароля')
    def navigate_to_profile_page(self) -> ProfilePage:
        self.click_to_element(MainPageLocators.LINK_PROFILE)
        
        profile_page = ProfilePage(self.driver)
        if profile_page.is_page_loaded():
            return profile_page
        raise AssertionError
    
    def is_auth(self):
        if self.find_visible_element(MainPageLocators.BUTTON_CREATE_ORDER):
            return True
        return False
    
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(MainPageLocators.LINK_CONSTRUCTOR)
        ]
        return all(conditions)