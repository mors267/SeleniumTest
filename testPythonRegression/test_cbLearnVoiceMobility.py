import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
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

def test_ShopPlansWithPhoneButtonHero(driver):

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    #validate correct URl is present
    if "https://business.comcast.com/shop/offers" in element: 
        print('Shop plans with phone button available on page') 
    else: 
        print('Shop plans with phone button NOT available on page')  
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div/div[4]/a').get_attribute('href'))

def test_SeeItInAction(driver): 

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    #validate Home page Hero POI Modal is present on page#      
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > span > button').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/button').click()

    element = driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > span > button').text
    assert element == 'SEE IT IN ACTION'

    if "SEE IT IN ACTION" in element: 
        print('Video link available on homepage hero') 
    else: 
        print('Video link NOT available on homepage hero')  


def test_JumpLinks(driver):  

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

#features jump link

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(1) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#features > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Boost communication and collaboration'

    if "Boost communication and collaboration" in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page') 

#your phone at work jump link  

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(2) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#ideal-for > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Put your Phone features to work'

    if "Put your Phone features to work" in element: 
        print('Your Phone At Work section available on page') 
    else: 
        print('Your Phone At Work  NOT available on page')

#solutions jump link 

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#solutions > div > div > div:nth-child(1) > div > p').text
    assert element == 'THE COMPLETE SOLUTION'

    if "THE COMPLETE SOLUTION" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page') 

#Compare Phone Services jump link

    click_button = driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a')
    click_button.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value='#compare > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Explore and compare all our Phone services'

    if "Explore and compare all our Phone services" in element: 
        print('Compare phone services section available on page') 
    else: 
        print('Compare phone services section NOT available on page')

#Req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[5]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#lead-form-container > div > legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead form available on page') 
    else: 
        print('Lead form NOT available on page') 

#Get pricing jump link 

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[6]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#plans-pricing > div > div > div > div > h2').text
    assert element == 'Let’s find some deals in your area'

    if "Let’s find some deals in your area" in element: 
        print('Get Pricing Section available on page') 
    else: 
        print('Get Pricing Section NOT available on page') 


def test_AppStoreLinks(driver):  

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    #apple store link
    driver.find_element(by=By.XPATH, value='//*[@id="ideal-for"]/div[2]/div/div[1]/div/div[1]/p[4]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='body > div.ember-view > main > div.animation-wrapper.is-visible > section.l-content-width.section.section--hero.product-hero > div > div.l-column.small-7.medium-8.large-9.small-valign-top > header > h1').text
    assert element == 'Comcast Business 4+'

    if "Comcast Business 4+" in element: 
        print('Apple store link available') 
    else: 
        print('Apple store link NOT available')

    driver.back()

    #google play link
    driver.find_element(by=By.CSS_SELECTOR, value='#ideal-for > div.primary-2-up > div > div:nth-child(1) > div > div.rich-text.primary-2-up-rich-text > p:nth-child(4) > span > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value="//span[@class='AfwdI']").text
    assert element == 'Comcast Business'

    if "Comcast Business" in element: 
        print('Google play link available') 
    else: 
        print('Google play link NOT available')

def test_SolutionsSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    #Business Internet
    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet'

    if "https://business.comcast.com/learn/internet" in element: 
        print('Business Internet link available on page') 
    else: 
        print('Business Internet link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href'))   

    #SecurityEdge
    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/security-edge'

    if "https://business.comcast.com/learn/internet/security-edge" in element: 
        print('SecurityEdge link available on page') 
    else: 
        print('SecurityEdge link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))   

    #ConnectionPro 
    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/connection-pro-automatic-backup'

    if "https://business.comcast.com/learn/internet/connection-pro-automatic-backup" in element: 
        print('Connection Pro link available on page') 
    else: 
        print('Connection Pro link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[3]/a').get_attribute('href'))   

    #wifiPro
    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/wifi-pro'

    if "https://business.comcast.com/learn/internet/wifi-pro" in element: 
        print('WiFi Pro link available on page') 
    else: 
        print('WiFi Pro link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[4]/a').get_attribute('href'))   


def test_HMDlink(driver):

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@class='button button-tertiary']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/solution-finder'

    if "https://business.comcast.com/learn/solution-finder" in element: 
        print('HMD link available on page') 
    else: 
        print('HMD link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@class='button button-tertiary']").get_attribute('href'))   


def test_ExploreCompareChartRadioButtons(driver):  

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    #capacity radio button

    driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tbody/tr[1]/th/button').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/div/div/div').text
    assert element == 'A Business Voice line is one number per line, typically tied to one user. A Business VoiceEdge seat is similar but with added features and the flexibility to be assigned to a desk or conference room. Trunks refer to the number of concurrent calls used at any given time.'

    if "A Business Voice line is one number per line, typically tied to one user. A Business VoiceEdge seat is similar but with added features and the flexibility to be assigned to a desk or conference room. Trunks refer to the number of concurrent calls used at any given time." in element: 
        print('Capacity radio button content displaying correctly') 
    else: 
        print('Capacity radio button content NOT displaying')

    driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/button').click()

    #Phone system radio button

    driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tbody/tr[3]/th/button').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/div/div/div').text
    assert element == 'A hosted PBX solution has uniform features for companies who have a set number of seats. A Cloud PBX is a virtual network that can scale with staff growth and multiple locations.'

    if "A hosted PBX solution has uniform features for companies who have a set number of seats. A Cloud PBX is a virtual network that can scale with staff growth and multiple locations." in element: 
        print('Phone system radio button content displaying correctly') 
    else: 
        print('Phone system radio button content NOT displaying')  

    driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/button').click()

    #Mobility feature radio button

    driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tbody/tr[4]/th/button').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/div/div/div').text
    assert element == 'This lets you know if a service includes anywhere calling features.'

    if "This lets you know if a service includes anywhere calling features." in element: 
        print('Mobility feature radio button content displaying correctly') 
    else: 
        print('Mobility feature radio button content NOT displaying')  

    driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/button').click()

def test_ExploreCompareChartLinks(driver):

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

#voice mobility
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    if "https://business.comcast.com/shop/offers" in element: 
        print('VoiceMobility Shop Now link available on chart') 
    else: 
        print('VoiceMobility Shop Now link NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[1]/a').get_attribute('href'))

#business voiceedge
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voiceedge-virtual-pbx'

    if "https://business.comcast.com/learn/phone/voiceedge-virtual-pbx" in element: 
        print('VoiceEdge Learn More link available on chart') 
    else: 
        print('VoiceEdge Learn More link NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[2]/a').get_attribute('href'))    

#pri trunks
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/pri-trunks'

    if "https://business.comcast.com/learn/phone/pri-trunks" in element: 
        print('PRI trunks Learn More link available on chart') 
    else: 
        print('PRI trunks Learn More link NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[3]/a').get_attribute('href'))    


#sip trunks
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/sip-trunks'

    if "https://business.comcast.com/learn/phone/sip-trunks" in element: 
        print('SIP trunks Learn More link available on chart') 
    else: 
        print('SIP trunks Learn More link NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[4]/a').get_attribute('href'))   


def test_ViewPlansPricingLink(driver):

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value='//*[@id="plans-pricing"]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    if "https://business.comcast.com/shop/offers" in element: 
        print('view plans and pricing link available on page') 
    else: 
        print('view plans and pricing NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="plans-pricing"]/div/div/div/div/div[2]/a').get_attribute('href'))  

def test_ComcastMobileLink(driver):

    driver.get('https://business.comcast.com/learn/phone/voice-mobility?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//div[contains(@class,'container--wide cb-theme-light')]//a[contains(@class,'button button-primary')]").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile'

    if "https://business.comcast.com/learn/mobile" in element: 
        print('CBM link available on page') 
    else: 
        print('CBM link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[contains(@class,'container--wide cb-theme-light')]//a[contains(@class,'button button-primary')]").get_attribute('href'))
