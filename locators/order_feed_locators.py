from selenium.webdriver.common.by import By


class OrderFeedLocators:
    LINK_ORDER_FEED = By.XPATH, ".//a[@aria-current='page']/p[text()='Лента Заказов']"