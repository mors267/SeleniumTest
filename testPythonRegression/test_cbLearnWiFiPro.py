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

    driver.get('https://business.comcast.com/learn/internet/wifi-pro/?disablescripts=true')
    driver.maximize_window()

#features jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="features"]/div[1]/div[1]/div[2]/div/h3').text
    assert element == 'Faster WiFi for guests. More control for you.'

    #validate text is present on page#
    if "Faster WiFi for guests. More control for you." in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page') 


#solutions jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/h3').text
    assert element == 'More ways to help you stay protected'

    if "More ways to help you stay protected" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page') 

#req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page') 

#get pricing jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="get pricing"]/div/div/div/div/h2').text
    assert element == 'Let’s find some deals in your area'

    if "Let’s find some deals in your area" in element: 
        print('Get Pricing section available on page') 
    else: 
        print('Get Pricing section NOT available on page')

    #click on shop now button on Hero

def test_ShopNowButtonHero(driver):

    driver.get('https://business.comcast.com/learn/internet/wifi-pro/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    #validate correct URl is present
    if "https://business.comcast.com/shop/offers" in element: 
        print('ShopNow button available on page') 
    else: 
        print('ShopNow button NOT available on page')  
    print("CTA URL: "+driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > a').get_attribute('href'))

    #See it in action video link

def test_SeeItInAction(driver): 

    driver.get('https://business.comcast.com/learn/internet/wifi-pro/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > span > button').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/button').click()

    element = driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > span > button').text
    assert element == 'SEE IT IN ACTION'

    if "SEE IT IN ACTION" in element: 
        print('Video link available on homepage hero') 
    else: 
        print('Video link NOT available on homepage hero')


def test_SolutionsSectionLink(driver):

    driver.get('https://business.comcast.com/learn/internet/wifi-pro/?disablescripts=true')
    driver.maximize_window()

#business internet link

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet'

    if "https://business.comcast.com/learn/internet" in element: 
        print('Business Internet link available on page') 
    else: 
        print('Business Internet link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[1]/a').get_attribute('href'))

#security edge link

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/security-edge'

    if "https://business.comcast.com/learn/internet/security-edge" in element: 
        print('SecurityEdge™ link available on page') 
    else: 
        print('SecurityEdge™ link NOT available on page')  
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[2]/a').get_attribute('href'))

#connection pro link

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/connection-pro-automatic-backup'

    if "https://business.comcast.com/learn/internet/connection-pro-automatic-backup" in element: 
        print('Connection Pro link available on page') 
    else: 
        print('Connection Pro link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[3]/a').get_attribute('href'))


def test_ViewPlansPricingLink(driver):

    driver.get('https://business.comcast.com/learn/internet/wifi-pro/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value='//*[@id="get pricing"]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    if "https://business.comcast.com/shop/offers" in element: 
        print('view plans and pricing link available on page') 
    else: 
        print('view plans and pricing NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="get pricing"]/div/div/div/div/div[2]/a').get_attribute('href'))  
