import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_HomepageLOBTiles(browser):
    # Load the URL
    browser.get('https://business.comcast.com/?disablescripts=true')
    browser.maximize_window()
    browser.refresh()

    # Define elements and their expected href values
    elements = {
        "//a[@href='/learn/mobile']": 'https://business.comcast.com/learn/mobile',
        "//a[@href='/learn/internet']": 'https://business.comcast.com/learn/internet',
        "//a[@href='/learn/phone']": 'https://business.comcast.com/learn/phone',
        "//a[@href='/learn/internet/security-edge']": 'https://business.comcast.com/learn/internet/security-edge'
    }

    # Loop through elements, assert href value, and print result
    for xpath, expected_href in elements.items():
        element = browser.find_element(By.XPATH, xpath)
        assert element.get_attribute('href') == expected_href
        print('\n' + xpath + ' href value matches expected URL')
        print("CTA URL:", element.get_attribute('href'))
        


