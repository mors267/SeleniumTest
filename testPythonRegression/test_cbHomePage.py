import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
import time
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920, 1200))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors"
]

for option in options:
    chrome_options.add_argument(option)


@pytest.fixture(scope="module")    
def driver():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit() 

def test_HomepageLOBTiles(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    # Define elements and their expected href values
    elements = {
        "//a[@href='/learn/mobile']": 'https://business.comcast.com/learn/mobile',
        "//a[@href='/learn/internet']": 'https://business.comcast.com/learn/internet',
        "//a[@href='/learn/phone']": 'https://business.comcast.com/learn/phone',
        "//a[@href='/learn/internet/security-edge']": 'https://business.comcast.com/learn/internet/security-edge'
    }

    # Loop through elements, assert href value, and print result
    for xpath, expected_href in elements.items():
        element = driver.find_element(By.XPATH, xpath)
        assert element.get_attribute('href') == expected_href
        print('\n' + xpath + ' href value matches expected URL')
        print("CTA URL:", element.get_attribute('href'))
        
def test_HomepageHMDSection(driver):
    # Load the URL
    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    # Find and assert href value for HMD section
    element = driver.find_element(By.CSS_SELECTOR, '.button.button--lg.button-tertiary.button-tertiary--no-border')
    assert element.get_attribute('href') == 'https://business.comcast.com/learn/solution-finder'
    print('HMD link available in section')
    print("CTA URL:", element.get_attribute('href'))
