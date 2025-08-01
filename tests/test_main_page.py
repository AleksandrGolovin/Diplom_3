import allure


@allure.title('Тестовые сценарии главной страницы')
class TestMainPage:
    
    @allure.title('Проверка перехода на главную страницу (конструктор) с ленты заказов по кнопке')
    @allure.description('')
    def test_main_page_open_from_order_feed_page_success(self, order_feed_page):
        order_feed_page.open()
        
        main_page = order_feed_page.navigate_to_main_page()
        
        assert main_page.is_loaded()
    
    @allure.title('Проверка появления окна с деталями ингредиента')
    @allure.description('')
    def test_main_page_click_ingredient_details_popup_displayed(self, main_page):
        main_page.open()
        
        main_page.click_random_ingredient()
        
        assert main_page.is_details_popup_displayed()
        
    @allure.title('Проверка закрытия окна с деталями ингредиента')
    @allure.description('')
    def test_main_page_close_details_popup_not_displayed(self, main_page):
        main_page.open()
        main_page.click_random_ingredient()
        
        main_page.close_details_popup()
        
        assert not main_page.is_details_popup_displayed()
        
    @allure.title('Проверка добавления ингредиента в бургер (увелиние количества)')
    @allure.description('')
    def test_main_page_add_ingredient_increased_count(self, main_page):
        main_page.open()
        
        is_success = main_page.add_ingredient_to_order()
        
        assert is_success