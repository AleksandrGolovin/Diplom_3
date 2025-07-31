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

    def find_element_with_wait(self, locator):
        "Найти элемент на странице"
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except:
            return None

    def click_to_element(self, locator):
        "Кликнуть на элемент на странице"
        link = self.wait.until(ec.element_to_be_clickable(locator))
        try:
            self.driver.find_element(*locator).click()
        except:
            self.driver.execute_script("arguments[0].click();", link)

    def set_text_to_element(self, locator, text):
        "Передать текст в элемент ввода"
        element = self.find_element_with_wait(locator)
        if element:
            element.send_keys(text)
    
    def get_text_from_element(self, locator):
        "Получить текст элемента"
        element = self.find_element_with_wait(locator)
        if element:
            text = element.text
            return text
        return None

    def scroll_to_element(self, locator):
        "Пролистать страницу до элемента"
        element = self.find_element_with_wait(locator)
        if element:
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
            except:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
    def switch_to_last_tab(self):
        "Переключиться на последнюю вкладку"
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def wait_for_url(self, url_part):
        "Подождать загрузки URL, в котором содержится искомый фрагмент"
        self.wait.until(ec.url_contains(url_part))