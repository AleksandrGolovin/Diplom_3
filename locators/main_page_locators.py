from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_CONSTRUCTOR_ACTIVE = By.XPATH, ".//a[@aria-current='page']/p[text()='Конструктор']"
    BUTTON_CREATE_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"
    LINK_INGREDIENTS = By.XPATH, "(.//a[contains(@class, 'BurgerIngredient_ingredient')])"
    SECTION_INGREDIENT_DETAILS = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"
    SECTION_CONSTRUCTOR_BASKET = By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]"
    BUTTON_POPUP_CLOSE = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button"