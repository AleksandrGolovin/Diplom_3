from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_PROFILE = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href='/account']"
    LINK_CONSTRUCTOR = By.XPATH, ".//a[@aria-current='page']/p[text()='Конструктор']"