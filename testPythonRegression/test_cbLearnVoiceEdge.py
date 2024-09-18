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

def test_JumpLinks(driver):  

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
    driver.maximize_window()

#Features jump link  

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(1) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#features > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Cloud-hosted PBX service that helps you go further'

    if "Cloud-hosted PBX service that helps you go further" in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page') 

#Apps jump link  

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(2) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#apps > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Apps to power communication and collaboration'

    if "Apps to power communication and collaboration" in element: 
        print('Apps section available on page') 
    else: 
        print('Apps NOT available on page')

#phone options jump link

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(3) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#phones > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Devices available to lease'

    if "Devices available to lease" in element: 
        print('Phone Options section available on page') 
    else: 
        print('Phone Options NOT available on page')

#solutions jump link 

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(4) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#compare > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Explore and compare all our Phone services'

    if "Explore and compare all our Phone services" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page') 

#req a quote jump link

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(5) > a').click()

    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//legend[@class='headline-4']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Lead form did not display')

    element = driver.find_element(by=By.XPATH, value="//legend[@class='headline-4']").text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead form section available') 
    else: 
        print('Lead form section NOT available')

def test_AppStoreLinks(driver):  

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
    driver.maximize_window()

    #apple store link
    driver.find_element(by=By.XPATH, value='//*[@id="apps"]/div[2]/div/div[1]/div/div[1]/p[2]/a[1]/img').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='body > div.ember-view > main > div.animation-wrapper.is-visible > section.l-content-width.section.section--hero.product-hero > div > div.l-column.small-7.medium-8.large-9.small-valign-top > header > h1').text
    assert element == 'Comcast Business 4+'

    if "Comcast Business 4+" in element: 
        print('Apple store link available') 
    else: 
        print('Apple store link NOT available')

    driver.back()

    #google play link
    driver.find_element(by=By.CSS_SELECTOR, value='#apps > div:nth-child(2) > div > div:nth-child(1) > div > div.rich-text.primary-2-up-rich-text > p:nth-child(3) > a:nth-child(2) > img').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value="//span[@class='AfwdI']").text
    assert element == 'Comcast Business'

    if "Comcast Business" in element: 
        print('Google play link available') 
    else: 
        print('Google play link NOT available')


def test_HelpAndSupportArticlelink(driver):

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value='//*[@id="apps"]/div[3]/div/div[2]/div/div[1]/p[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/support/article/voice/download-and-use-the-business-voiceedge-companion-app'

    if "https://business.comcast.com/support/article/voice/download-and-use-the-business-voiceedge-companion-app" in element: 
        print('Help & Support article link available on page') 
    else: 
        print('Help & Support article link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="apps"]/div[3]/div/div[2]/div/div[1]/p[2]/a').get_attribute('href'))   


def test_ViewDemolink(driver):

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value='//*[@id="apps"]/div[3]/div/div[2]/div/a').get_attribute('href')
    assert element == 'http://cbappdemos.com/voiceedge/'

    if "http://cbappdemos.com/voiceedge/" in element: 
        print('VIEW DEMO link available on page') 
    else: 
        print('VIEW DEMO link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="apps"]/div[3]/div/div[2]/div/a').get_attribute('href'))     


def test_SolutionsLinks(driver):

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
    driver.maximize_window()

    #BusinessInternet link
    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet'

    if "https://business.comcast.com/learn/internet" in element: 
        print('Business Internet link available on page') 
    else: 
        print('Business Internet link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href'))    

    #SecurityEdge link    
    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/security-edge'

    if "https://business.comcast.com/learn/internet/security-edge" in element: 
        print('SecurityEdge link available on page') 
    else: 
        print('SecurityEdge link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))    

    #ConnectionPro link   
    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/connection-pro-automatic-backup'

    if "https://business.comcast.com/learn/internet/connection-pro-automatic-backup" in element: 
        print('Connection Pro link available on page') 
    else: 
        print('Connection Pro link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[3]/a').get_attribute('href'))    

    #WifiPro link   
    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/wifi-pro'

    if "https://business.comcast.com/learn/internet/wifi-pro" in element: 
        print('WiFi Pro link available on page') 
    else: 
        print('WiFi Pro link NOT available on on page')    
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[23]/div/div/div[1]/div/ul/li[4]/a').get_attribute('href'))    

def test_ExploreCompareChartRadioButtons(driver): 

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
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

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
    driver.maximize_window()

#voice mobility
    element = driver.find_element(by=By.XPATH, value="//div[@class='cb-table-wrap']//td[1]//a[1]").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voice-mobility'

    if "https://business.comcast.com/learn/phone/voice-mobility" in element: 
        print('VoiceMobility Learn More link available on chart') 
    else: 
        print('VoiceMobility Learn More NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[@class='cb-table-wrap']//td[1]//a[1]").get_attribute('href'))

#BusinessVoiceEdge
    element = driver.find_element(by=By.XPATH, value="//table[@class='cb-table-main']//a[@class='text-link text-link-secondary text-link-primary'][normalize-space()='GET A QUOTE']").text
    assert element == 'GET A QUOTE'

    if "GET A QUOTE" in element: 
        print('\n''Business VoiceEdge Get A Quote link available on chart') 
    else: 
        print('\n''Business VoiceEdge Get A Quote link NOT available on chart')      

#pri trunks
    element = driver.find_element(by=By.XPATH, value="//div[@class='cb-table-wrap']//td[3]//a[1]").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/pri-trunks'

    if "https://business.comcast.com/learn/phone/pri-trunks" in element:

        print('\n''PRITrunks learn more link available on chart') 
    else: 
        print('\n''PRITrunks learn more link NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[@class='cb-table-wrap']//td[3]//a[1]").get_attribute('href'))     

#sip trunks
    element = driver.find_element(by=By.XPATH, value="//div[@class='cb-table-wrap']//td[4]//a[1]").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/sip-trunks'

    if "https://business.comcast.com/learn/phone/sip-trunks" in element: 
        print('\n''SIP Trunks learn more link available on chart') 
    else: 
        print('\n''SIP Trunks learn more link NOT available on chart')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[@class='cb-table-wrap']//td[4]//a[1]").get_attribute('href'))   

def test_HMDlink(driver):

    driver.get('https://business.comcast.com/learn/phone/voiceedge-virtual-pbx?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[29]/div/div[2]/ul/li[2]/div[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/solution-finder'

    if "https://business.comcast.com/learn/solution-finder" in element: 
        print('HMD link available on page') 
    else: 
        print('HMD link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[29]/div/div[2]/ul/li[2]/div[3]/a').get_attribute('href'))  
