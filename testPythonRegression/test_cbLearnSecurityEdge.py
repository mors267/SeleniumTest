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

    driver.get('https://business.comcast.com/learn/internet/security-edge/?disablescripts=true')
    driver.maximize_window()

#cyberattack risks jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="cyberattack"]/div[1]/div/div/div/h2').text
    assert element == 'Cyberattacks can be costly'

    #validate text is present on page#
    if "Cyberattacks can be costly" in element: 
        print('Cyberattack section available on page') 
    else: 
        print('Cyberattack section NOT available on page') 

#features jump link  

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="features"]/div[1]/div/div/h2').text
    assert element == 'Advanced features that help you focus on business'

    if "Advanced features that help you focus on business" in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page')      

#solutions risks jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/h3').text
    assert element == 'More solutions to help you stay connected'

    if "More solutions to help you stay connected" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page') 

#req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value="//legend[contains(@class,'headline-4')]").text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page')

#get pricing jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[5]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a/span[2]').text
    assert element == 'Guest and private networks'

    if "Guest and private networks" in element: 
        print('Get Pricing section available on page') 
    else: 
        print('Get Pricing section NOT available on page')


def test_ShopNowButtonHero(driver):

    driver.get('https://business.comcast.com/learn/internet/security-edge/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div/div[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    if "https://business.comcast.com/shop/offers" in element: 
        print('ShopNow button available on hero') 
    else: 
        print('ShopNow button NOT available on hero')    
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div/div[4]/a').get_attribute('href'))   

def test_ValidateSolutionsSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/internet/security-edge/?disablescripts=true')
    driver.maximize_window()

#connection pro link

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/connection-pro-automatic-backup'

    if "https://business.comcast.com/learn/internet/connection-pro-automatic-backup" in element: 
        print('Connection Pro link available on page') 
    else: 
        print('Connection Pro link NOT available on page') 
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href'))   

#wifi pro link

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/wifi-pro'

    if "https://business.comcast.com/learn/internet/wifi-pro" in element: 
        print('WiFi Pro link available on page') 
    else: 
        print('WiFi Pro link NOT available on page')      
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))   


def test_ViewPlansPricingLink(driver):

    driver.get('https://business.comcast.com/learn/internet/security-edge/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@class='button button-primary']").get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers/?services=All&internetdownloadspeed=All&contractlength=All&price=All'

    if "https://business.comcast.com/shop/offers/?services=All&internetdownloadspeed=All&contractlength=All&price=All" in element: 
        print('VIEW PLANS AND PRICING link available on page') 
    else: 
        print('VIEW PLANS AND PRICING link NOT available on on page')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@class='button button-primary']").get_attribute('href'))   

