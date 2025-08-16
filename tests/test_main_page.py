import allure
import pytest


@allure.tag('main')
@allure.title('Тестовые сценарии главной страницы')
class TestMainPage:
    
    @allure.title('Проверка перехода на главную страницу (конструктор) с ленты заказов по кнопке')
    @allure.description('Открыть страницу ленты заказов, перейти на главную страницу, проверить загрузку главной страницы')
    def test_main_page_open_from_order_feed_page_success(self, order_feed_page):
        order_feed_page.open()
        
        main_page = order_feed_page.navigate_to_main_page()
        
        assert main_page.is_loaded()
    
    @allure.title('Проверка появления окна с деталями ингредиента')
    @allure.description('Открыть главную страницу, кликнуть на случайный ингредиент в списке, проверить отображение всплывающего окна с деталями ингредиента')
    def test_main_page_click_ingredient_details_popup_displayed(self, main_page):
        main_page.open()
        
        main_page.click_random_ingredient()
        
        assert main_page.is_details_popup_displayed()
        
    @allure.title('Проверка закрытия окна с деталями ингредиента')
    @allure.description('Открыть главную страницу, кликнуть на случайный ингредиент в списке, закрыть всплывающее окно с деталями ингредиента, проверить отсутствие всплывающего окна с деталями')
    def test_main_page_close_details_popup_not_displayed(self, main_page):
        main_page.open()
        main_page.click_random_ingredient()
        
        main_page.close_details_popup()
        
        assert not main_page.is_details_popup_displayed()
        
    @allure.description('Открыть главную страницу, добавить ингредиент к бургеру, проверить результат добавления')
    @pytest.mark.parametrize('type', ['bun', 'ingredient'])
    def test_main_page_add_ingredient_increased_count(self, type, main_page):
        allure.dynamic.title(f'Проверка добавления ингредиента типа {type} в бургер (увеличение количества)')
        main_page.open()
        
        is_success = main_page.add_ingredient_to_order(type)
        
        assert is_success

    @allure.description('Создать пользователя, открыть страницу логина, залогиниться созданным пользователем, создать заказ с параметром (количество ингредиентов), проверить результат создания')
    @pytest.mark.parametrize('ingredient_count', [0, 1, 3])
    def test_main_page_create_order_auth_success(self, ingredient_count, create_user, login_page):
        allure.dynamic.title(f'Проверка создания заказа с count={ingredient_count} ingredient (соус или котлета) в бургере')
        email, password = create_user()
        login_page.open()        
        main_page = login_page.auth(email, password)
        is_success, order_number = main_page.create_new_order(ingredient_count)

        assert all([
            is_success,
            order_number != '9999'  # Есть вероятность, что еще раз счетчик перейдет 9999?
        ])