from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    "Базовая страница для наследования остальными страницами типовых методов"
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        "Перейти на страницу по адресу"
        self.driver.get(url)

    def find_visible_element(self, locator):
        "Найти элемент на странице"
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except:
            return None

    def scroll_to_element(self, locator):
        """Пролистать страницу до элемента"""
        element = self.find_visible_element(locator)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_to_element(self, locator):
        """Кликнуть на элемент на странице"""
        element = self.wait.until(ec.element_to_be_clickable(locator))
        self.scroll_to_element(locator)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def set_text_to_element(self, locator, text):
        "Передать текст в элемент ввода"
        element = self.find_visible_element(locator)
        if element:
            element.send_keys(text)
    
    def get_text_from_element(self, locator):
        "Получить текст элемента"
        element = self.find_visible_element(locator)
        if element:
            text = element.text
            return text
        return None
        
    def switch_to_last_tab(self):
        "Переключиться на последнюю вкладку"
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def wait_for_url(self, url_part):
        "Подождать загрузки URL, в котором содержится искомый фрагмент"
        self.wait.until(ec.url_contains(url_part))

    def _verify_page_loaded(self):
        """Метод для проверки загрузки страницы (требует переопределения)"""
        pass

    def is_page_loaded(self):
        """Публичный метод для проверки загрузки страницы"""
        try:
            self._verify_page_loaded()
            return True
        except:
            return False