import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get('http://www.comcastbusiness.com')
print(driver.title)

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
