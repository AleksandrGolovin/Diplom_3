import pytest
import requests
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from helpers import generate_unique_email
from data import URL


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = request.param
    
    driver_instance = None
    
    browser_width = 1400
    browser_height = 800
    
    if browser == 'firefox':
        # Настройки Firefox
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--private")
        firefox_options.add_argument(f"--width={browser_width}")
        firefox_options.add_argument(f"--height={browser_height}")
        driver_instance = webdriver.Firefox(options=firefox_options)
    elif browser == 'chrome':
        # Настройки Chrome
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument(f"--window-size={browser_width},{browser_height}")
        driver_instance = webdriver.Chrome(options=chrome_options)
    
    yield driver_instance
    
    # Завершение работы драйвера
    driver_instance.quit() # type: ignore

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)

@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture
def create_user():
    """
    Фикстура для создания пользователя и его последующего удаления
    """
    users_to_delete = []

    def _create_user():
        # Генерируем данные пользователя
        email = generate_unique_email()
        password = 'password'
        name = "Test User"
        
        # Собираем payload
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        
        # Делаем запрос на создание
        response = requests.post(
            url=f'{URL.API_AUTH}/register',
            json=payload
        )

        # Сохраняем учетные данные для последующего удаления пользователя
        users_to_delete.append((email, password))

        return email, password
    
    yield _create_user
    
    # Удаляем пользователей после выполнения тестов
    for email, password in users_to_delete:
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(
            url=f'{URL.API_AUTH}/login',
            json=payload
        )
        if response.status_code == 200:
            access_token = response.json()["accessToken"]
            headers = {"Authorization": f"{access_token}"}
            response = requests.delete(
                url=f'{URL.API_AUTH}/user',
                headers=headers
            )