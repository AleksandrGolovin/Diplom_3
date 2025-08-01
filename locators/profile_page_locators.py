from selenium.webdriver.common.by import By


class ProfilePageLocators:
    LINK_PROFILE = By.XPATH, ".//a[text()='Профиль']"
    LINK_HISTORY = By.XPATH, ".//a[text()='История заказов']"
    LINK_LOGOUT = By.XPATH, ".//a[text()='Выход']"
    TEXT_PROFILE_HINT = By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']"