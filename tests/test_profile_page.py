import allure


@allure.tag('profile')
@allure.title('Тестовые сценарии страницы профиля')
class TestProfilePage:
    
    @allure.title('Проверка перехода на страницу профиля')
    @allure.description('Создать пользователя, перейти на страницу логина, авторизоваться под созданным пользователем, перейти на страницу профиля, проверить загрузку страницы профиля')
    def test_profile_page_open_success(self, create_user, login_page):
        email, password = create_user()
        login_page.open()
        main_page = login_page.auth(email, password)
        
        profile_page = main_page.navigate_to_profile_page()
        
        assert profile_page.is_loaded()
        
    @allure.title('Проверка перехода в историю заказов')
    @allure.description('Создать пользователя, перейти на страницу логина, авторизоваться под созданным пользователем, создать заказ, перейти на страницу профиля, перейти в историю заказов, проверить загрузку истории заказов')
    def test_profile_page_show_orders_history_success(self, create_user, login_page):
        email, password = create_user()
        login_page.open()
        main_page = login_page.auth(email, password)
        main_page.create_new_order()
        profile_page = main_page.navigate_to_profile_page()
        
        profile_page.show_orders_history()
        
        assert profile_page.is_orders_history_displayed()

    @allure.title('Проверка выхода из профиля')
    @allure.description('Создать пользователя, перейти на страницу логина, авторизоваться под созданным пользователем, перейти на страницу профиля, выйти из профиля по кнопке выхода, проверить загрузку страницы логина')
    def test_profile_page_logout_success(self, create_user, login_page):
        email, password = create_user()
        login_page.open()
        main_page = login_page.auth(email, password)
        profile_page = main_page.navigate_to_profile_page()
        
        profile_page.logout()
        
        assert login_page.is_loaded()