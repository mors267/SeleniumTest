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

    driver.get('https://business.comcast.com/learn/phone/sip-trunks/?disablescripts=true')
    driver.maximize_window()

#features jump link

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(1) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#standard-features > div:nth-child(1) > div > p').text
    assert element == 'STANDARD FEATURES'

    if "STANDARD FEATURES" in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page') 

#Trunking jump link

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(2) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#continuity-features > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Continuity features to keep the phone lines open'

    if "Continuity features to keep the phone lines open" in element: 
        print('Trunking at work section available on page') 
    else: 
        print('Trunking at work section NOT available on page')

#Solutions options jump link   

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(3) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#solutions > div > div > div:nth-child(1) > div > p').text
    assert element == 'SINGLE-SOURCE PROVIDER'

    if "SINGLE-SOURCE PROVIDER" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page')

#compare phone jump link         

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(4) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#comparison-chart > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Explore and compare all our Phone Services'

    if "Explore and compare all our Phone Services" in element: 
        print('Compare phone section available on page') 
    else: 
        print('Compare phone section NOT available on page') 
        
        
#req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[5]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page') 

def test_HeroGetQuoteLink(driver):

    driver.get('https://business.comcast.com/learn/phone/sip-trunks/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-hero-pdp.alj-theme > div > div.ra-hero-button-row > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#lead-form-container > div > legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('GetaQuote button available on hero') 
    else: 
        print('GetaQuote button NOT available on hero')   

def test_SolutionsLinks(driver):

    driver.get('https://business.comcast.com/learn/phone/sip-trunks/?disablescripts=true')
    driver.maximize_window()

    #BusinessInternet link
    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet'

    if "https://business.comcast.com/learn/internet" in element: 
        print('Business Internet link available on page') 
    else: 
        print('Business Internet link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href'))    

    #SecurityEdge link    
    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/security-edge'

    if "https://business.comcast.com/learn/internet/security-edge" in element: 
        print('SecurityEdge link available on page') 
    else: 
        print('SecurityEdge link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))    

def test_ExploreCompareChartRadioButtons(driver):  

    driver.get('https://business.comcast.com/learn/phone/sip-trunks/?disablescripts=true')
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

    element = driver.find_element(by=By.CSS_SELECTOR, value='#modal-standard > div.cb-modal.cb-modal--center > div > div > div').text
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
    assert element == 'This lets you know if a service includes anywhere calling features. '

    if "This lets you know if a service includes anywhere calling features. " in element: 
        print('Mobility feature radio button content displaying correctly') 
    else: 
        print('Mobility feature radio button content NOT displaying')  

    driver.find_element(by=By.XPATH, value='//*[@id="modal-standard"]/div[2]/button').click()


def test_ExploreCompareChartLinks(driver):

    driver.get('https://business.comcast.com/learn/phone/sip-trunks/?disablescripts=true')
    driver.maximize_window()

    #voice mobility
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voice-mobility'

    if "https://business.comcast.com/learn/phone/voice-mobility" in element: 
        print('VoiceMobility Learn More link available on chart') 
    else: 
        print('VoiceMobility Learn More NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[1]/a').get_attribute('href'))       

    #voiceedge
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voiceedge-virtual-pbx'

    if "https://business.comcast.com/learn/phone/voiceedge-virtual-pbx" in element: 
        print('VoiceEdge Learn More link available on chart') 
    else: 
        print('VoiceEdge Learn More NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[2]/a').get_attribute('href'))         

    #pri trunks
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/pri-trunks'

    if "https://business.comcast.com/learn/phone/pri-trunks" in element: 
        print('PRITrunks Quote link available on chart') 
    else: 
        print('PRITrunks Quote link NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[3]/a').get_attribute('href'))     

    #sip trunks
    element = driver.find_element(by=By.CSS_SELECTOR, value='#cb-table-scroll > div > table > tfoot > tr > td.highlighted > a').text
    assert element == 'GET A QUOTE'

    if "GET A QUOTE" in element: 
        print('SIPTrunks Get a Quote link available on chart') 
    else: 
        print('SIPTrunks get a quote link NOT available on chart')

def test_ExploreCBMLink(driver):

    driver.get('https://business.comcast.com/learn/phone/sip-trunks/?disablescripts=true')
    driver.maximize_window()

    #BusinessInternet link
    element = driver.find_element(by=By.LINK_TEXT, value='EXPLORE COMCAST BUSINESS MOBILE').text
    assert element == "EXPLORE COMCAST BUSINESS MOBILE"

    if "EXPLORE COMCAST BUSINESS MOBILE" in element: 
        print('Explore CBM link available on page') 
    else: 
        print('Explore CBM link NOT available on on page')
