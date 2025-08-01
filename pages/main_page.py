import allure
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators
from data import URL


class MainPage(BasePage):
    def open(self):
        self.go_to_url(URL.MAIN_PAGE)
        return self
    
    def _verify_page_loaded(self):
        link_constructor_active = self.find_visible_element(MainPageLocators.LINK_CONSTRUCTOR)
        return all([link_constructor_active])
    
    @allure.step('Переход на страницу личного кабинета пароля')
    def navigate_to_profile_page(self) -> ProfilePage:
        self.click_to_element(MainPageLocators.LINK_PROFILE)
        
        profile_page = ProfilePage(self.driver)
        if profile_page.is_page_loaded():
            return profile_page
        raise AssertionError