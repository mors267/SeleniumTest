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

    driver.get('https://business.comcast.com/learn/tv/hotels/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@class='button']").get_attribute('title')
    assert element == 'REQUEST A QUOTE'

    #validate correct URl is present
    if "REQUEST A QUOTE" in element: 
        print('Request a Quote CTA available on hero') 
    else: 
        print('Request a Quote CTA NOT available on hero')  

def test_FeaturesJumpLink(driver):

    driver.get('https://business.comcast.com/learn/tv/hotels/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="plan-grid"]/div/div/div[2]/div/h3').text
    assert element == 'Nothing standard about your business — or X1 for Hospitality'

    if "Nothing standard about your business — or X1 for Hospitality" in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page')

    #req a quote CTA

    driver.find_element(by=By.XPATH, value="//a[@class='button button-primary']").click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value="//legend[@class='headline-4']").text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('RequestAQuote CTA available on section') 
    else: 
        print('RequestAQuote CTA NOT available on section')

def test_SolutionsSectionJumpLink(driver):

    driver.get('https://business.comcast.com/learn/tv/hotels/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value="//p[contains(@class,'eyebrow')]").text
    assert element == 'PERFECT PAIRINGS'

    if "PERFECT PAIRINGS" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page')

#business internet link

    element = driver.find_element(by=By.XPATH, value="//span[@class='cb-tile-card-title'][normalize-space()='Business Internet']").text
    assert element == 'Business Internet'

    if "Business Internet" in element: 
        print('\n''Business Internet link available on section') 
    else: 
        print('\n''Business Internet link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href'))

#Phone solutions link

    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Phone Solutions']").text
    assert element == 'Phone Solutions'

    if "Phone Solutions" in element: 
        print('\n''Phone solutions link available on section') 
    else: 
        print('\n''Phone solutions link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))

def test_ReqAQuoteJumpLink(driver):

    driver.get('https://business.comcast.com/learn/tv/hotels/?disablescripts=true')
    driver.maximize_window()
    
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page') 
