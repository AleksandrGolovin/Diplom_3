import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from data import URL


class OrderFeedPage(BasePage):
    BASE_URL = URL.ORDER_FEED_PAGE
    
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(OrderFeedLocators.LINK_ORDER_FEED)
        ]
        return all(conditions)