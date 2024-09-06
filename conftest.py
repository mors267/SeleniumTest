import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import allure

@pytest.fixture()
def setup(request):
    options = Options()
    options.page_load_strategy = 'normal'
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()