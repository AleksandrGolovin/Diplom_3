import allure
import random
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.general_locators import GeneralLocators
from data import URL


class OrderFeedPage(BasePage):
    BASE_URL = URL.ORDER_FEED_PAGE
    
    def _get_random_order_locator(self, type='bun'):
        orders_locator = OrderFeedLocators.LINK_ORDERS
        self.wait_for_visibility(orders_locator)
        orders = self.driver.find_elements(*orders_locator)
        orders_count = len(orders)
        if orders_count > 0:
            index = random.randint(1, orders_count)
            random_locator = orders_locator[0], f'{orders_locator[1]}[{index}]'
            return random_locator
        else:
            raise AssertionError
    
    @allure.step('Нажатие на случайный ингредиент из списка')
    def click_random_order(self):
        locator = self._get_random_order_locator()
        self.wait_for_visibility(locator)
        self.click_to_element(locator)
            
    def is_details_popup_displayed(self):
        try:
            self.find_visible_element(OrderFeedLocators.SECTION_ORDER_DETAILS)
            return True
        except:
            return False
    
    def is_order_exists(self, order_number):
        orders_locator = OrderFeedLocators.LINK_ORDERS
        self.wait_for_visibility(orders_locator)
        orders = self.driver.find_elements(*orders_locator)
        found = any(order.text.splitlines()[0] == order_number for order in orders)
        return found
    
    def get_orders_global_counter(self):
        self.wait_for_visibility(OrderFeedLocators.P_ORDERS_GLOBAL_COUNTER)
        return self.get_text_from_element(OrderFeedLocators.P_ORDERS_GLOBAL_COUNTER)
    
    def get_orders_today_counter(self):
        self.wait_for_visibility(OrderFeedLocators.P_ORDERS_TODAY_COUNTER)
        return self.get_text_from_element(OrderFeedLocators.P_ORDERS_TODAY_COUNTER)
    
    def get_order_in_progress(self):
        order_number_locator = OrderFeedLocators.LI_ORDERS_IN_PROGRESS
        self.wait_for_visibility(order_number_locator)
        self.wait.until_not(lambda d: self.get_text_from_element(order_number_locator) == 'Все текущие заказы готовы!')
        order_number = self.get_text_from_element(order_number_locator)
        return order_number
    
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