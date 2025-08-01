import allure


@allure.title('Тестовые сценарии страницы логина')
class TestLoginPage:
    
    @allure.title('Проверка перехода на страницу логина')
    @allure.description('')
    def test_login_page_open_success(self, login_page):
        login_page.open()
        
        assert login_page.is_loaded()
        
    @allure.title('Проверка перехода на страницу логина')
    @allure.description('')
    def test_login_page_auth_success(self, create_user, login_page):
        email, password = create_user()
        login_page.open()
        
        main_page = login_page.auth(email, password)
        
        assert all([
            main_page.is_loaded(),  # Проверка загрузки главной страницы
            main_page.is_auth()  # Проверка наличия авторизации
        ])