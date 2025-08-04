import allure


@allure.tag('password_restore')
@allure.title('Тестовые сценарии страницы сброса пароля')
class TestResetPasswordPage:
    
    @allure.title('Проверка ввода почты и клика по кнопке подтверждения восстановления пароля')
    @allure.description('Открыть страницу восстановления пароля, ввести email, перейти на страницу сброса пароля, проверить загрузку страницы сброса пароля')
    def test_reset_password_enter_email_and_submit_success(self, forgot_password_page):
        forgot_password_page.open()
        forgot_password_page.enter_email()
        reset_password_page = forgot_password_page.navigate_to_reset_password_page()
        
        assert reset_password_page.is_loaded()
        
    @allure.title('Проверка активации окна ввода при нажатии кнопки отображения пароля')
    @allure.description('Открыть страницу восстановления пароля, ввести email, перейти на страницу сброса пароля, проверить активность окна ввода пароля при клике на кнопку отображения пароля')
    def test_reset_password_show_password_input_activate_by_click_success(self, forgot_password_page):
        forgot_password_page.open()
        forgot_password_page.enter_email()
        reset_password_page = forgot_password_page.navigate_to_reset_password_page()
        
        assert reset_password_page.is_password_input_activate_by_click()