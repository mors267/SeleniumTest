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

def test_ReqAQuoteButtonHero(driver):

    driver.get('https://business.comcast.com/learn/tv/public/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > a').get_attribute('title')
    assert element == 'REQUEST A QUOTE'

    #validate correct URl is present
    if "REQUEST A QUOTE" in element: 
        print('Request a Quote CTA available on hero') 
    else: 
        print('Request a Quote CTA NOT available on hero')  

def test_PlanAndPricingJumpLink(driver):

    driver.get('https://business.comcast.com/learn/tv/public/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="plans"]/div[1]/div/div/div/h2').text
    assert element == 'So much content — and easy voice control for all of it '

    if "So much content — and easy voice control for all of it " in element: 
        print('Plan Pricing section available on page') 
    else: 
        print('Plan pricing section NOT available on page')

    #req a quote CTA

    driver.find_element(by=By.XPATH, value='//*[@id="plans"]/div[2]/div/div/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('RequestAQuote CTA available on section') 
    else: 
        print('RequestAQuote CTA NOT available on section')

    #View Channel lineup link

    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[10]/div/div/div[2]/div/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/channel-lineup'

    if "https://business.comcast.com/learn/tv/channel-lineup" in element: 
        print('VIEW CHANNEL LINEUP link available on section') 
    else: 
        print('VIEW CHANNEL LINEUP link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[10]/div/div/div[2]/div/a').get_attribute('href'))

def test_AddOnsJumpLink(driver):

    driver.get('https://business.comcast.com/learn/tv/public/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="add-ons"]/div[1]/div/div/div/h2').text
    assert element == 'Customize — for customer satisfaction'

    if "Customize — for customer satisfaction" in element: 
        print('Add-Ons section available on page') 
    else: 
        print('Add-Ons section NOT available on page')


    #req a quote CTA

    driver.find_element(by=By.XPATH, value='//*[@id="add-ons"]/div[3]/div/div/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('RequestAQuote CTA available on section') 
    else: 
        print('RequestAQuote CTA NOT available on section')

def test_X1FeaturesJumpLink(driver):

    driver.get('https://business.comcast.com/learn/tv/public/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="x1features"]/div/div/div[1]/div/h3').text
    assert element == 'X1 for Business: the ultimate entertainment experience'

    if "X1 for Business: the ultimate entertainment experience" in element: 
        print('X1 features section available on page') 
    else: 
        print('X1 features section NOT available on page')

def test_SolutionsSectionJumpLink(driver):

    driver.get('https://business.comcast.com/learn/tv/public/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="related-resources"]/div/div/div[1]/div/h3').text
    assert element == 'Now complete your TV solution'

    if "Now complete your TV solution" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page')

#business internet link

    element = driver.find_element(by=By.XPATH, value='//*[@id="related-resources"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet'

    if "https://business.comcast.com/learn/internet" in element: 
        print('Business Internet link available on section') 
    else: 
        print('Business Internet link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="related-resources"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href'))

#Wifi pro link

    element = driver.find_element(by=By.XPATH, value='//*[@id="related-resources"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/wifi-pro'

    if "https://business.comcast.com/learn/internet/wifi-pro" in element: 
        print('WifiPro link available on section') 
    else: 
        print('WifiPro link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="related-resources"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))

def test_HMDlink(driver):

    driver.get('https://business.comcast.com/learn/tv/public/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[22]/div/div[2]/ul/li[2]/div[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/solution-finder'

    if "https://business.comcast.com/learn/solution-finder" in element: 
        print('HMD link available on page') 
    else: 
        print('HMD link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[22]/div/div[2]/ul/li[2]/div[3]/a').get_attribute('href'))
