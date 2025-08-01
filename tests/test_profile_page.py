import allure
from data import CREDENTIALS


@allure.title('Тестовые сценарии страницы профиля')
class TestProfilePage:
    
    @allure.title('Проверка перехода на страницу профиля')
    @allure.description('')
    def test_profile_page_open_success(self, login_page):
        login_page.open()
        main_page = login_page.auth(*CREDENTIALS)
        profile_page = main_page.navigate_to_profile_page()
        
        assert profile_page.is_page_loaded()