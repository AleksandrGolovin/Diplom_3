import allure
from data import CREDENTIALS


@allure.title('Тестовые сценарии страницы логина')
class TestLoginPage:
    
    @allure.title('Проверка перехода на страницу логина')
    @allure.description('')
    def test_login_page_open_success(self, login_page):
        login_page.open()
        
        assert login_page.is_page_loaded()
        
    @allure.title('Проверка перехода на страницу логина')
    @allure.description('')
    def test_login_page_auth_success(self, login_page):
        login_page.open()
        main_page = login_page.auth(*CREDENTIALS)
        
        assert all([
            main_page.is_page_loaded(),  # Проверка загрузки главной страницы
            main_page.is_auth()  # Проверка наличия авторизации
        ])