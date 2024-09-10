import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

options = Options()
options.add_argument("--headless");
options.add_argument("--window-size=1920, 1080")


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_ShopInternetDropDownLinks(driver):
    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()
    driver.refresh()

    #view all offers link
    element = driver.find_element(By.XPATH, "//span[normalize-space()='VIEW ALL OFFERS']")
    assert element.get_attribute('href') == 'https://business.comcast.com/shop/offers?services=All&internetdownloadspeed=All&contractlength=All&price=All'
    print('View all offer link available in global header')
    print("CTA URL:", element.get_attribute('href'))

    #HMD link
    element = driver.find_element(By.XPATH, "//div[@class='HMD__bar-link-cta']")
    assert element.get_attribute('href') == 'https://business.comcast.com/learn/solution-finder'
    print('HMD link available in global header')
    print("CTA URL:", element.get_attribute('href'))

    #internet link
    element = driver.find_element(By.XPATH, "//a[@id='business-internet-header-id']//span[@class='bsd-nav-link-text'][normalize-space()='Business Internet']")
    assert element.get_attribute('href') == 'https://business.comcast.com/learn/internet'
    print('Internet link available in global header')
    print("CTA URL:", element.get_attribute('href'))
