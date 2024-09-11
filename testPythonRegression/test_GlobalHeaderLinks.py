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

def test_ShopMobileDropDownLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

#Mobile link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile'

    if "https://business.comcast.com/learn/mobile" in element: 
        print('Mobile link available in shop global header') 
    else: 
        print('Mobile link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-header-id"]').get_attribute('href'))

    #Plan link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile/plan'

    if "https://business.comcast.com/learn/mobile/plan" in element: 
        print('\n''Plan link available in shop global header') 
    else: 
        print('Plan link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[1]/a').get_attribute('href'))    

    #Network link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile/network-coverage'

    if "https://business.comcast.com/learn/mobile/network-coverage" in element: 
        print('\n''Network link available in shop global header') 
    else: 
        print('Network link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[2]/a').get_attribute('href'))    

    #Phones link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/mobile?category=device'

    if "https://business.comcast.com/shop/mobile?category=device" in element: 
        print('\n''Phones link available in shop global header') 
    else: 
        print('Phones link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[3]/a').get_attribute('href')) 

    #Tablets link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/mobile?category=tablet'

    if "https://business.comcast.com/shop/mobile?category=tablet" in element: 
        print('\n''Tablets link available in shop global header') 
    else: 
        print('Tablets link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[4]/a').get_attribute('href'))

    #Smart watches link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/mobile?category=smart_watch'

    if "https://business.comcast.com/shop/mobile?category=smart_watch" in element: 
        print('\n''Smart watches link available in shop global header') 
    else: 
        print('Smart watches link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[5]/a').get_attribute('href'))                

    #Accessories link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/mobile?category=accessories'

    if "https://business.comcast.com/shop/mobile?category=accessories" in element: 
        print('\n''Accessories link available in shop global header') 
    else: 
        print('Accessories link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[6]/a').get_attribute('href'))

    #Bring your phone link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[7]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile/byod'

    if "https://business.comcast.com/learn/mobile/byod" in element: 
        print('\n''Byod link available in shop global header') 
    else: 
        print('Byod link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[7]/a').get_attribute('href'))  

    #Deals link
    element = driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[8]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile/deals'

    if "https://business.comcast.com/learn/mobile/deals" in element: 
        print('\n''Deals link available in shop global header') 
    else: 
        print('Deals link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="mobile-list-id"]/li[8]/a').get_attribute('href')) 

def test_ShopPhoneDropDownLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #Phone link
    element = driver.find_element(by=By.XPATH, value='//*[@id="phone-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone'

    if "https://business.comcast.com/learn/phone" in element: 
        print('Phone link available in shop global header') 
    else: 
        print('Phone link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="phone-header-id"]').get_attribute('href'))

    #VoiceMobility link
    element = driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voiceedge-mobility'

    if "https://business.comcast.com/learn/phone/voiceedge-mobility" in element: 
        print('\n''VoiceMobility link available in shop global header') 
    else: 
        print('VoiceMobility link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[1]/a').get_attribute('href'))

    #BusinessVoiceEdge link
    element = driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voiceedge-virtual-pbx'

    if "https://business.comcast.com/learn/phone/voiceedge-virtual-pbx" in element: 
        print('\n''BusinessVoiceEdge link available in shop global header') 
    else: 
        print('BusinessVoiceEdge link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[2]/a').get_attribute('href'))              

    #PRI Trunks link
    element = driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/pri-trunks'

    if "https://business.comcast.com/learn/phone/pri-trunks" in element: 
        print('\n''PRI Trunks link available in shop global header') 
    else: 
        print('PRI Trunks link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[3]/a').get_attribute('href')) 

    #SIP Trunks link
    element = driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/sip-trunks'

    if "https://business.comcast.com/learn/phone/sip-trunks" in element: 
        print('\n''SIP Trunks link available in shop global header') 
    else: 
        print('SIP Trunks link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="phone-list-id"]/li[4]/a').get_attribute('href')) 

def test_ShopBusinessTvDropDownLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #BusinessTv link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv'

    if "https://business.comcast.com/learn/tv" in element: 
        print('BusinessTv link available in shop global header') 
    else: 
        print('BusinessTv link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="phone-header-id"]').get_attribute('href'))

    #Public view TV link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/public'

    if "https://business.comcast.com/learn/tv/public" in element: 
        print('\n''Public view TV link available in shop global header') 
    else: 
        print('Public view TV link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[1]/a').get_attribute('href'))

    #Bar Restaurant TV link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/bars-restaurants'

    if "https://business.comcast.com/learn/tv/bars-restaurants" in element: 
        print('\n''Bar Restaurant TV link available in shop global header') 
    else: 
        print('Bar Restaurant TV link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[2]/a').get_attribute('href'))

    #Private view TV link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/private'

    if "https://business.comcast.com/learn/tv/private" in element: 
        print('\n''Private view TV link available in shop global header') 
    else: 
        print('Private view TV link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[3]/a').get_attribute('href'))

    #In Room Entertainment TV link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/hotels'

    if "https://business.comcast.com/learn/tv/hotels" in element: 
        print('\n''In Room Entertainment TV link available in shop global header') 
    else: 
        print('In Room Entertainment TV link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[4]/a').get_attribute('href'))

    #Channel Lineup link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/Channel-Lineup'

    if "https://business.comcast.com/learn/tv/Channel-Lineup" in element: 
        print('\n''Channel Lineup link available in shop global header') 
    else: 
        print('Channel Lineup link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-list-id"]/li[5]/a').get_attribute('href'))


def test_ShopCloudAppsDropDownLinks(driver): 

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #Cloudapps link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/cloud'

    if "https://business.comcast.com/learn/cloud" in element: 
        print('Cloudapps link available in shop global header') 
    else: 
        print('Cloudapps link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-header-id"]').get_attribute('href'))

    #Nortion security link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/144963/norton-security-for-professionals'

    if "https://cloudsolutions.comcast.com/en-US/apps/144963/norton-security-for-professionals" in element: 
        print('\n''Nortion security link available in shop global header') 
    else: 
        print('Nortion security link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[1]/a').get_attribute('href'))

    #Microsoft365 link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/145167/microsoft-365-business'

    if "https://cloudsolutions.comcast.com/en-US/apps/145167/microsoft-365-business" in element: 
        print('\n''Microsoft365 link available in shop global header') 
    else: 
        print('Microsoft365 link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[2]/a').get_attribute('href'))

    #ecomfax link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/144858/ecomfax'

    if "https://cloudsolutions.comcast.com/en-US/apps/144858/ecomfax" in element: 
        print('\n''ecomfax link available in shop global header') 
    else: 
        print('ecomfax link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[3]/a').get_attribute('href'))

    #voiceEdge desktop app link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/support/article/voice/download-and-use-the-business-voiceedge-companion-app'

    if "https://business.comcast.com/support/article/voice/download-and-use-the-business-voiceedge-companion-app" in element: 
        print('\n''voiceEdge desktop app link available in shop global header') 
    else: 
        print('voiceEdge desktop app link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[4]/a').get_attribute('href'))

    #View all apps desktop app link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/home'

    if "https://cloudsolutions.comcast.com/en-US/home" in element: 
        print('\n''View all apps link available in shop global header') 
    else: 
        print('View all apps link NOT available in shop global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-apps-list-id"]/li[5]/a').get_attribute('href'))

