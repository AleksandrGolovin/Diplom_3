import allure


@allure.title('Тестовые сценарии страницы ленты заказов')
class TestOrderFeedPage:
    
    @allure.title('Проверка перехода на страницу ленты заказов с главной страницы по кнопке')
    @allure.description('')
    def test_order_feed_page_open_from_main_page_success(self, main_page):
        main_page.open()
        
        order_feed_page = main_page.navigate_to_order_feed_page()
        
        assert order_feed_page.is_loaded()
        
    # @allure.title('Проверка перехода на страницу логина')
    # @allure.description('')
    # def test_login_page_auth_success(self, create_user, login_page):
    #     email, password = create_user()
    #     login_page.open()
        
    #     main_page = login_page.auth(email, password)
        
    #     assert all([
    #         main_page.is_page_loaded(),  # Проверка загрузки главной страницы
    #         main_page.is_auth()  # Проверка наличия авторизации
    #     ])