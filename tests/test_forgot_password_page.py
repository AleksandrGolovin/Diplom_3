import allure


@allure.title('Тестовые сценарии страницы восстановления пароля')
class TestForgotPasswordPage:
    
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('')
    def test_forgot_password_page_open_success(self, login_page):
        login_page.open()
        forgot_password_page = login_page.navigate_to_forgot_password_page()
        
        assert forgot_password_page.is_page_loaded()