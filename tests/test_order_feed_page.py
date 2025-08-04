import allure


@allure.title('Тестовые сценарии страницы ленты заказов')
class TestOrderFeedPage:
    
    @allure.title('Переход на страницу ленты заказов с главной страницы по кнопке')
    @allure.description('')
    def test_order_feed_page_open_from_main_page_success(self, main_page):
        main_page.open()
        
        order_feed_page = main_page.navigate_to_order_feed_page()
        
        assert order_feed_page.is_loaded()
        
    @allure.title('Появление окна с деталями заказа')
    @allure.description('')
    def test_order_feed_page_order_details_popup_displayed(self, order_feed_page):
        order_feed_page.open()
        
        order_feed_page.click_random_order()
        
        assert order_feed_page.is_details_popup_displayed()
        
    @allure.title('Наличие заказа из Истории Заказов пользователя в Ленте Заказов')
    @allure.description('')
    def test_order_feed_page_user_order_history_in_order_feed_contains(self, login_page, create_user):
        email, password = create_user()
        login_page.open()        
        main_page = login_page.auth(email, password)
        main_page.create_new_order()
        profile_page = main_page.navigate_to_profile_page()
        order_number = profile_page.get_last_order_number_from_history()
        order_feed_page = profile_page.navigate_to_order_feed_page()
        
        assert order_feed_page.is_order_exists(order_number)
        
    @allure.title('Увеличение глобального счетчика заказов')
    @allure.description('')
    def test_order_feed_page_create_order_global_counter_increased(self, login_page, create_user):
        email, password = create_user()
        login_page.open()        
        main_page = login_page.auth(email, password)
        order_feed_page = main_page.navigate_to_order_feed_page()
        global_counter_before = order_feed_page.get_orders_global_counter()
        order_feed_page.navigate_to_main_page()
        main_page.create_new_order()
        main_page.navigate_to_order_feed_page()
        global_counter_after = order_feed_page.get_orders_global_counter()
        
        assert global_counter_after > global_counter_before
        
    @allure.title('Увеличение счетчика заказов за сегодня')
    @allure.description('')
    def test_order_feed_page_create_order_today_counter_increased(self, login_page, create_user):
        email, password = create_user()
        login_page.open()        
        main_page = login_page.auth(email, password)
        order_feed_page = main_page.navigate_to_order_feed_page()
        today_counter_before = order_feed_page.get_orders_today_counter()
        order_feed_page.navigate_to_main_page()
        main_page.create_new_order()
        main_page.navigate_to_order_feed_page()
        today_counter_after = order_feed_page.get_orders_today_counter()
        
        assert today_counter_after > today_counter_before
        
    @allure.title('Наличие заказа в списке "В работе"')
    @allure.description('')
    def test_order_feed_page_create_order_progress_list_contains_order(self, login_page, create_user):
        email, password = create_user()
        login_page.open()        
        main_page = login_page.auth(email, password)
        _, order_create_number = main_page.create_new_order()
        order_feed_page = main_page.navigate_to_order_feed_page()
        oreder_in_progress_number = order_feed_page.get_order_in_progress()
        
        assert int(oreder_in_progress_number) == int(order_create_number)