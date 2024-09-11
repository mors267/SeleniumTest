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

def test_JumpLinks(driver):

    driver.get('https://business.comcast.com/learn/internet/connection-pro-automatic-backup/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value='//*[@id="features"]/div[1]/div/div/h2').text
    assert element == 'Great connections are good business'

    #validate text is present on page#
    if "Great connections are good business" in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page') 

#Solutions jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value='//*[@id="Solutions"]/div/div/div[2]/div/h3').text
    assert element == 'Next-level security'

    if "Next-level security" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page') 

#Req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()       
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page') 

#get pricing jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()       
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value='//*[@id="plans-pricing"]/div/div/div/div/div[1]').text
    assert element == 'Shop plans available in your area now — most offers can be ordered online with professional installation available with convenient appointment windows. '

    if "Shop plans available in your area now — most offers can be ordered online with professional installation available with convenient appointment windows. " in element: 
        print('Get Pricing section available on page') 
    else: 
        print('Get Pricing section NOT available on page')

    #click on shop now button on Hero

def test_ShopNowButtonHero(driver):

    driver.get('https://business.comcast.com/learn/internet/connection-pro-automatic-backup/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@title='shop now']").get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    #validate text is present on page#
    if "https://business.comcast.com/shop/offers" in element: 
        print('ShopNow button available on hero') 
    else: 
        print('ShopNow button NOT available on hero')  

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@title='shop now']").get_attribute('href'))


def test_ValidateSolutionsLink(driver):

    driver.get('https://business.comcast.com/learn/internet/connection-pro-automatic-backup/?disablescripts=true')
    driver.maximize_window()

#business internet link

    element = driver.find_element(by=By.XPATH, value="//span[@class='cb-tile-card-title'][normalize-space()='Business Internet']").text
    assert element == 'Business Internet'

    if "Business Internet" in element: 
        print('Business Internet link available on page') 
    else: 
        print('Business Internet link NOT available on page')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="Solutions"]/div/div/div[2]/div/ul/li[1]/a').get_attribute('href'))

#SecurityEdgelink

    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='SecurityEdge']").text
    assert element == 'SecurityEdge'

    if "SecurityEdge" in element: 
        print('\n''SecurityEdge link available on page') 
    else: 
        print('\n''SecurityEdge link NOT available on page')  

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="Solutions"]/div/div/div[2]/div/ul/li[2]/a').get_attribute('href'))

#WifiPro

    element = driver.find_element(by=By.XPATH, value="//span[@class='cb-tile-card-title'][normalize-space()='WiFi Pro']").text
    assert element == 'WiFi Pro'

    if "WiFi Pro" in element: 
        print('\n''WiFi Pro link available on page') 
    else: 
        print('\n''WiFi Pro link NOT available on page')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="Solutions"]/div/div/div[2]/div/ul/li[3]/a').get_attribute('href'))


def test_ViewPlansPricingLink(driver):

    driver.get('https://business.comcast.com/learn/internet/connection-pro-automatic-backup/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@class='button button-primary']").get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    if "https://business.comcast.com/shop/offers" in element: 
        print('VIEW PLANS AND PRICING link available on page') 
    else: 
        print('VIEW PLANS AND PRICING link NOT available on on page')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@class='button button-primary']").get_attribute('href'))
