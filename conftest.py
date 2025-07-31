import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions


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