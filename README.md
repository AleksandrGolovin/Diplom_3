# Diplom_3: Stellar Burgers UI Testing

## Описание проекта
Проект представляет собой автоматизированные UI-тесты для сервиса **Stellar Burgers**. Тесты охватывают ключевые сценарии работы веб-интерфейса:
- Авторизация и выход из системы
- Восстановление и сброс пароля
- Работа с конструктором бургеров
- Формирование и отслеживание заказов
- Управление профилем пользователя

Тесты реализованы на Python с использованием:
- `Selenium` для автоматизации браузера
- `Pytest` как тестовый фреймворк
- `Allure` для формирования отчетов
- `Requests` для API-взаимодействия
- Параметризация тестов для проверки различных состояний системы

## Тестовые классы и методы

### test_login_page.py
**Класс**: TestLoginPage  
Тесты страницы авторизации:
- `test_login_page_open_success`: Проверка открытия страницы логина
- `test_login_page_auth_success`: Проверка успешной авторизации пользователя

### test_forgot_password_page.py
**Класс**: TestForgotPasswordPage  
Тесты восстановления пароля:
- `test_forgot_password_page_open_success`: Проверка перехода на страницу восстановления пароля

### test_reset_password_page.py
**Класс**: TestResetPasswordPage  
Тесты сброса пароля:
- `test_reset_password_enter_email_and_submit_success`: Ввод почты и переход на страницу сброса
- `test_reset_password_show_password_input_activate_by_click_success`: Активация поля ввода пароля

### test_main_page.py
**Класс**: TestMainPage  
Тесты главной страницы:
- `test_main_page_open_from_order_feed_page_success`: Переход на главную страницу из ленты заказов
- `test_main_page_click_ingredient_details_popup_displayed`: Отображение деталей ингредиента
- `test_main_page_close_details_popup_not_displayed`: Закрытие окна деталей ингредиента
- `test_main_page_add_ingredient_increased_count`: Добавление ингредиента в заказ
- `test_main_page_create_order_auth_success`: Создание заказа с разным количеством ингредиентов

### test_order_feed_page.py
**Класс**: TestOrderFeedPage  
Тесты ленты заказов:
- `test_order_feed_page_open_from_main_page_success`: Открытие ленты заказов
- `test_order_feed_page_order_details_popup_displayed`: Детали заказа во всплывающем окне
- `test_order_feed_page_user_order_history_in_order_feed_contains`: Проверка истории заказов
- `test_order_feed_page_create_order_global_counter_increased`: Увеличение общего счетчика заказов
- `test_order_feed_page_create_order_today_counter_increased`: Увеличение дневного счетчика заказов
- `test_order_feed_page_create_order_progress_list_contains_order`: Проверка статуса "В работе"

### test_profile_page.py
**Класс**: TestProfilePage  
Тесты профиля пользователя:
- `test_profile_page_open_success`: Открытие страницы профиля
- `test_profile_page_show_orders_history_success`: Проверка истории заказов
- `test_profile_page_logout_success`: Выход из системы

## Ключевые компоненты

### Фикстуры (conftest.py)
- `driver`: Инициализация Chrome/Firefox (параметризованный выбор)
- `forgot_password_page`, `order_feed_page`, `login_page`, `profile_page`, `main_page`: Инициализация Page Object Model
- `create_user`: Создание и удаление тестового пользователя через API

### Data (data.py)
Класс `URL` содержит адреса всех ключевых страниц

### Helpers (helpers.py)
Содержит метод `generate_unique_email()` для генерации уникального адреса электронной почты

## Установка и запуск

### Установка зависимостей
Установите необходимые пакеты из файла `requirements.txt` командой:  
> `pip install -r requirements.txt`

### Запуск тестов
Выполните команду:  
> `pytest --alluredir=allure_results`

### Просмотр отчета Allure
1. Запустите сервер с отчетом:  
> `allure serve allure_results`

2. Для генерации статического отчета:  
> `allure generate allure_results -o allure_report --clean`

После этого откройте файл `allure_report/index.html` в браузере.

## Структура проекта
Основные компоненты проекта:
```
Diplom_3/
├── locators/              # Локаторы элементов
├── pages/                 # Page Object Model
├── tests/                 # Тестовые сценарии
├── conftest.py            # Фикстуры Pytest
├── data.py                # URL и константы
├── helpers.py             # Вспомогательные функции
└── requirements.txt       # Зависимости
```
Тесты проверяют как базовую функциональность интерфейса, так и комплексные пользовательские сценарии с интеграцией между разными разделами приложения.
