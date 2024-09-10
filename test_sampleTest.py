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
        
