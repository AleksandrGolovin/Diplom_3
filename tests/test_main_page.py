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
        
        is_success = main_page.add_ingredient_to_order('bun')
        
        assert is_success

    @allure.title('Проверка создания заказа')
    @allure.description('')
    def test_main_page_create_order_auth_success(self, create_user, login_page):
        email, password = create_user()
        login_page.open()        
        main_page = login_page.auth(email, password)
        is_success, order_number = main_page.create_new_order()

        assert all([
            is_success,  # По таймауту может не успеть?
            order_number != '9999'  # Есть вероятность, что еще раз счетчик перейдет 9999?
        ])