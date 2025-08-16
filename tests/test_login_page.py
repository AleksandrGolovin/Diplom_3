import allure


@allure.tag('login')
@allure.title('Тестовые сценарии страницы логина')
class TestLoginPage:
    
    @allure.title('Проверка открытия страницы логина')
    @allure.description('Открыть страницу логина, проверить загрузку страницы логина')
    def test_login_page_open_success(self, login_page):
        login_page.open()
        
        assert login_page.is_loaded()
        
    @allure.title('Проверка авторизации пользователя')
    @allure.description('Создать пользователя, перейти на страницу логина, авторизоваться созданным пользователем, проверить результат авторизации и загрузку главной страницы')
    def test_login_page_auth_success(self, create_user, login_page):
        email, password = create_user()
        login_page.open()
        
        main_page = login_page.auth(email, password)
        
        assert all([
            main_page.is_loaded(),  # Проверка загрузки главной страницы
            main_page.is_auth()  # Проверка наличия авторизации
        ])