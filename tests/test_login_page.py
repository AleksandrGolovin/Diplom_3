import allure


@allure.title('Тестовые сценарии страницы логина')
class TestLoginPage:
    
    @allure.title('Проверка перехода на страницу логина')
    @allure.description('')
    def test_open_login_page_success(self, login_page):
        login_page.open()
        
        assert login_page.is_page_loaded()