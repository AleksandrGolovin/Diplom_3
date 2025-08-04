import allure
import random
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.general_locators import GeneralLocators
from data import URL


class MainPage(BasePage):
    BASE_URL = URL.MAIN_PAGE
    
    def _get_random_ingredient_locator(self, type='bun'):
        ingredient_locator = MainPageLocators.LINK_INGREDIENTS
        self.wait_for_visibility(ingredient_locator)  # Подождать появления списка ингредиентов
        ingredients = self.driver.find_elements(*ingredient_locator)  # Получить все элементы списка ингредиентов
        ingredients_count = len(ingredients)
        # Если список ингредиентов не пустой, то выбрать случайный (по типу)
        if ingredients_count > 0:
            index = 0
            if type == 'bun':
                index = random.randint(1, 2)  # 1..2 ингредиенты - булки
            elif type == 'ingredient':
                index = random.randint(3, ingredients_count)  # 3+ ингредиенты - соусы и котлеты
            else:
                raise TypeError
            random_locator = ingredient_locator[0], f'{ingredient_locator[1]}[{index}]'  # Дополнить локатор
            return random_locator
        else:
            raise AssertionError
    
    @allure.step('Нажатие на случайный ингредиент из списка')
    def click_random_ingredient(self):
        locator = self._get_random_ingredient_locator('ingredient')
        self.wait_for_visibility(locator)
        self.click_to_element(locator)

    @allure.step('Статус проверки отображения всплывающего окна')
    def is_details_popup_displayed(self):
        try:
            self.driver.find_element(*MainPageLocators.SECTION_INGREDIENT_DETAILS)
            return True
        except:
            return False
    
    @allure.step('Закрыть всплывающее окно')
    def close_details_popup(self):
        self.click_to_element(MainPageLocators.BUTTON_POPUP_CLOSE)
        self.wait_for_invisibility(MainPageLocators.SECTION_INGREDIENT_DETAILS)

    @allure.step('Drag and Drop элементов страницы')
    def drag_and_drop_element(self, locator_from, locator_to):
        element_from = self.wait_for_visibility(locator_from)
        self.scroll_to_element(locator_from)
        element_to = self.wait_for_visibility(locator_to)
        self.driver.execute_script(
            """
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            """,
        element_from,
        element_to
    )

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self, type='bun'):
        locator_from = self._get_random_ingredient_locator(type)
        ingredint_count_locator = locator_from[0], f'{locator_from[1]}/div[1]/p'
        ingredient_count_before = self.get_text_from_element(ingredint_count_locator)  # На пустом бургере == 0 
        locator_to = MainPageLocators.SECTION_CONSTRUCTOR_BASKET
        self.drag_and_drop_element(locator_from, locator_to)  # Добавление ингредиентов перетаскиванием
        ingredient_count_after = self.get_text_from_element(ingredint_count_locator)
        
        # Проверяем, что число ингредиентов изменилось
        ingredient_count_diff = 0
        if type == 'bun':
            ingredient_count_diff = 2
        elif type == 'ingredient':
            ingredient_count_diff = 1
        else:
            raise TypeError
        
        # Если удалось получить количество ингредиентов, то проверяем разницу ДО и ПОСЛЕ
        if ingredient_count_before and ingredient_count_after:
            return int(ingredient_count_after) - int(ingredient_count_before) == ingredient_count_diff
        else:
            raise AssertionError

    @allure.step('Создать новый заказ')
    def create_new_order(self, ingredient_count = 1):
        self.add_ingredient_to_order('bun')  # Без булки не собрать заказ
        
        # Повторить добавление ингредиентов ingredient_count раз
        for i in range(ingredient_count):
            self.add_ingredient_to_order('ingredient')
        
        self.click_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
        self.wait_for_visibility(MainPageLocators.IMG_TICK_ANIMATION)
        number_locator = MainPageLocators.H2_ORDER_NUMBER_TITLE
        order_number_default = self.get_text_from_element(number_locator)  # Номер заказа по умолчанию
        try:
            # Ожидание получения номера заказа
            self.wait.until_not(lambda d: self.get_text_from_element(number_locator) == order_number_default)
            result = True, self.get_text_from_element(number_locator)
            self.close_details_popup()  # Закрыть окно с деталями заказа
            return result
        except:
            return False, self.get_text_from_element(number_locator)

    @allure.step('Переход на страницу личного кабинета по клику на профиль')
    def navigate_to_profile_page(self):
        self.click_to_element(GeneralLocators.LINK_PROFILE)
        
        from pages.profile_page import ProfilePage
        destination_page = ProfilePage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError
    
    @allure.step('Переход на страницу ленты заказов по клику на ленту заказов')
    def navigate_to_order_feed_page(self):
        self.click_to_element(GeneralLocators.LINK_ORDER_FEED)
        
        from pages.order_feed_page import OrderFeedPage
        destination_page = OrderFeedPage(self.driver)
        if destination_page.is_loaded():
            return destination_page
        raise AssertionError
    
    @allure.step('Статус проверки на авторизацию')
    def is_auth(self):
        if self.find_visible_element(MainPageLocators.BUTTON_CREATE_ORDER):
            return True
        return False
    
    @allure.step('Проверка, что страница открылась')
    def _verify_page_loaded(self):
        conditions = [
            self.find_visible_element(MainPageLocators.LINK_CONSTRUCTOR_ACTIVE)
        ]
        return all(conditions)