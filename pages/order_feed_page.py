import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.general_locators import GeneralLocators
from data import URL


class OrderFeedPage(BasePage):
    BASE_URL = URL.ORDER_FEED_PAGE
    
    @allure.step('Переход на главную')
    def navigate_to_main_page(self):
        self.click_to_element(GeneralLocators.LINK_CONSTRUCTOR)
        
        from pages.main_page import MainPage
        destination_page = MainPage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError
    
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(OrderFeedLocators.LINK_ORDER_FEED_ACTIVE)
        ]
        return all(conditions)