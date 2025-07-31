import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.title('Тестовые сценарии страницы восстановления пароля')
class TestResetPasswordPage:
    
    @allure.title('Проверка ввода почты и клика по кнопке подтверждения восстановления пароля')
    @allure.description('')
    def test_enter_email_and_submit_success(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page()
        forgot_password_page.enter_email()
        reset_password_page = forgot_password_page.submit_restore()
        
        assert reset_password_page.check_reset_password_page()
        
    @allure.title('Проверка активации окна ввода при нажатии кнопки отображения пароля')
    @allure.description('')
    def test_password_input_activate_by_click_success(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page()
        forgot_password_page.enter_email()
        reset_password_page = forgot_password_page.submit_restore()
        
        assert reset_password_page.check_password_input_activate_by_click()