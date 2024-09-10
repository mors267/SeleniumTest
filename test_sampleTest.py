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

def test_ShopNowButtonHero(driver):
    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()
  
    #view all offers link
  
    element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[4]/a')
    assert element.get_attribute('href') == 'https://business.comcast.com/shop/offers'
    print('ShopNow button available on hero')
    print("CTA URL:", element.get_attribute('href'))

def test_SeeItInAction(driver):
    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value="//span[contains(text(),'SEE IT IN ACTION')]").click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//div[@class='cb-modal cb-modal-video']//span[@class='cb-text-icon cb-text-icon--close cb-text-icon--md']").click()

    element = driver.find_element(by=By.XPATH, value="//span[contains(text(),'SEE IT IN ACTION')]").text
    assert element == 'SEE IT IN ACTION'

    if "SEE IT IN ACTION" in element: 
        print('Video link available on homepage hero') 
    else: 
        print('Video link NOT available on homepage hero')  

def test_ReqAQuoteLink(driver): 

    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value="//button[@type='submit']").text
    assert element == 'GET STARTED'

    if "GET STARTED" in element: 
        print('Lead Gen available on page') 
    else: 
        print('Lead Gen NOT available on page') 

def test_JumpLinks(driver):  

    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()

#explore speeds jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//h2[normalize-space()='BUSINESS INTERNET STANDARD']").text
    assert element == 'BUSINESS INTERNET STANDARD'

    if "BUSINESS INTERNET STANDARD" in element: 
        print('Explore Speeds section available from jump link') 
    else: 
        print('Explore Speeds jump link not working') 

#solutions jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//h3[normalize-space()='Helping you stay connected plus protected']").text
    assert element == 'Helping you stay connected plus protected'

    if "Helping you stay connected plus protected" in element: 
        print('Solutions section available from jump link') 
    else: 
        print('Solutions jump link not working') 

#get a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//legend[@class='headline-4']").text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Get a quote section available from jump link') 
    else: 
        print('Get a quote jump link not working') 


#get pricing jump link  

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//h2[contains(text(),'Let’s find some deals in your area')]").text
    assert element == 'Let’s find some deals in your area'

    if "Let’s find some deals in your area" in element: 
        print('Get pricing section available from jump link') 
    else: 
        print('Get pricing jump link not working') 

def test_ShopInternetDropDownLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

#view all offers link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-meganav-panel-Shop"]/section/div[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers?services=All&internetdownloadspeed=All&contractlength=All&price=All'

    if "https://business.comcast.com/shop/offers?services=All&internetdownloadspeed=All&contractlength=All&price=All" in element: 
        print('View all offers link available in shop global header') 
    else: 
        print('view all offers link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-meganav-panel-Shop"]/section/div[1]/a').get_attribute('href'))

    #HMD link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-help-me-decide"]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/solution-finder'

    if "https://business.comcast.com/learn/solution-finder" in element: 
        print('\n''HMD link available in shop global header') 
    else: 
        print('HMD link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-help-me-decide"]/a').get_attribute('href'))  

    #internet link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet'

    if "https://business.comcast.com/learn/internet" in element: 
        print('\n''Internet link available in shop global header') 
    else: 
        print('Internet link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-header-id"]').get_attribute('href')) 

    #Wifi pro link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/wifi-pro'

    if "https://business.comcast.com/learn/internet/wifi-pro" in element: 
        print('\n''Wifi pro link available in shop global header') 
    else: 
        print('Wifi pro link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[1]/a').get_attribute('href')) 

    #Connection pro link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/connection-pro-automatic-backup'

    if "https://business.comcast.com/learn/internet/connection-pro-automatic-backup" in element: 
        print('\n''Connection pro link available in shop global header') 
    else: 
        print('Connection pro link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[2]/a').get_attribute('href')) 

    #SecurityEdge pro link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/security-edge'

    if "https://business.comcast.com/learn/internet/security-edge" in element: 
        print('\n''SecurityEdge link available in shop global header') 
    else: 
        print('SecurityEdge link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[3]/a').get_attribute('href'))    

    #Gig Speed network link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/gigabit-internet'

    if "https://business.comcast.com/learn/gigabit-internet" in element: 
        print('\n''Gig speed network link available in shop global header') 
    else: 
        print('Gig speed network link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[4]/a').get_attribute('href'))

    #internet Speed test link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet-speed-test'

    if "https://business.comcast.com/learn/internet-speed-test" in element: 
        print('\n''Internet speed test link available in shop global header') 
    else: 
        print('Internet speed test link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[5]/a').get_attribute('href'))
    
    #Ethernet dedicated link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/dedicated-internet'

    if "https://business.comcast.com/learn/internet/dedicated-internet" in element: 
        print('\n''Ethernet dedicated link available in shop global header') 
    else: 
        print('Ethernet dedicated test link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[6]/a').get_attribute('href'))
  
    #SD-Wan for Small Business link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[7]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/sd-wan-small-business'

    if "https://business.comcast.com/learn/internet/sd-wan-small-business" in element: 
        print('\n''SD-WAN for Small Business link available in shop global header') 
    else: 
        print('SD-Wan for Small Business link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-internet-list-id"]/li[7]/a').get_attribute('href'))

