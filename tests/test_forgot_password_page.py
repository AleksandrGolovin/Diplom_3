import allure
from pages.login_page import LoginPage


@allure.title('Тестовые сценарии страницы восстановления пароля')
class TestForgotPasswordPage:
    
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('')
    def test_open_forgot_password_page_success(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()
        forgot_password_page = login_page.navigate_to_forgot_password_page()
        
        assert forgot_password_page.check_forgot_password_page()