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

    driver.get('https://business.comcast.com/learn/phone/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[1]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="VOICE MOBILITY"]/div[2]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voice-mobility'

    if "https://business.comcast.com/learn/phone/voice-mobility" in element: 
        print('Voice Mobility link available on page') 
    else: 
        print('Voice Mobility link NOT available on page') 

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="VOICE MOBILITY"]/div[2]/div/ul/li/a').get_attribute('href'))    

#voiceEdge jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[1]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="voiceedge"]/div/div/div[1]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voiceedge-virtual-pbx'

    if "https://business.comcast.com/learn/phone/voiceedge-virtual-pbx" in element: 
        print('Voice Edge link available on page') 
    else: 
        print('Voice Edge link NOT available on page') 

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="voiceedge"]/div/div/div[1]/div/ul/li/a').get_attribute('href'))    

#trunking jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[1]/div/ul/li[3]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="trunking"]/div/div/div[2]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/pri-trunks'

    if "https://business.comcast.com/learn/phone/pri-trunks" in element: 
        print('PRI Trunks link available on page') 
    else: 
        print('PRI Trunks link NOT available on page') 

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="trunking"]/div/div/div[2]/div/ul/li/a').get_attribute('href'))    


#solutions jump link  

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[1]/div/ul/li[4]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="related-resources"]/div[1]/div/div/h2').text
    assert element == 'Industry insights'

    if "Industry insights" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page') 


#CBM jump link  

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[1]/div/ul/li[5]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="comcast business mobile"]/div/div/div[2]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile'

    if "https://business.comcast.com/learn/mobile" in element: 
        print('CBM link available on page') 
    else: 
        print('CBM link NOT available on page') 

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="comcast business mobile"]/div/div/div[2]/div/ul/li/a').get_attribute('href'))    

#req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[1]/div/ul/li[6]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page') 

def test_CBMLinkinExploreSection(driver):  

    driver.get('https://business.comcast.com/learn/phone/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Comcast Business Mobile']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile'

    if "https://business.comcast.com/learn/mobile" in element: 
        print('CBM link available on Explore Section') 
    else: 
        print('CBM link NOT available on Explore Section') 

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[normalize-space()='Comcast Business Mobile']").get_attribute('href'))            


def test_ExploreCompareChartRadioButtons(driver):  

    driver.get('https://business.comcast.com/learn/phone/?disablescripts=true')
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

    driver.get('https://business.comcast.com/learn/phone/?disablescripts=true')
    driver.maximize_window()

    #voice mobility
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voice-mobility'

    if "https://business.comcast.com/learn/phone/voice-mobility" in element: 
        print('Voice Mobility link available on chart') 
    else: 
        print('Voice Mobility link not available on chart') 

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[1]/a').get_attribute('href'))       

    #business voiceedge
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/voiceedge-virtual-pbx'

    if "https://business.comcast.com/learn/phone/voiceedge-virtual-pbx" in element: 
        print('BusinessVoiceEdge link available on chart') 
    else: 
        print('BusinessVoiceEdge link NOT available on chart')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[2]/a').get_attribute('href'))       

    #pri trunks
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/pri-trunks'

    if "https://business.comcast.com/learn/phone/pri-trunks" in element: 
        print('PRITrunks link available on chart') 
    else: 
        print('PRITrunks link NOT available on chart')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[3]/a').get_attribute('href'))       

    #sip trunks
    element = driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone/sip-trunks'

    if "https://business.comcast.com/learn/phone/sip-trunks" in element: 
        print('SIPTrunks link available on chart') 
    else: 
        print('SIPTrunks link NOT available on chart')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cb-table-scroll"]/div/table/tfoot/tr/td[4]/a').get_attribute('href'))       


def test_SpotlightSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/phone/?disablescripts=true')
    driver.maximize_window()

    #securityedge link

    element = driver.find_element(by=By.XPATH, value="//a[contains(text(),'SECURITYEDGE™')]").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/security-edge'

    if "https://business.comcast.com/learn/internet/security-edge" in element: 
        print('SECURITYEDGE link available in spotlight section') 
    else: 
        print('SECURITYEDGE link NOT available in spotlight section')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[contains(text(),'SECURITYEDGE™')]").get_attribute('href'))       

    #Connection pro link
    element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='CONNECTION PRO']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/connection-pro-automatic-backup'

    if "https://business.comcast.com/learn/internet/connection-pro-automatic-backup" in element: 
        print('CONNECTION PRO link available in spotlight section') 
    else: 
        print('CONNECTION PRO link NOT available in spotlight section')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[normalize-space()='CONNECTION PRO']").get_attribute('href'))       

    #Wifi pro link
    element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='WIFI PRO']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet/wifi-pro'

    if "https://business.comcast.com/learn/internet/wifi-pro" in element: 
        print('WIFI PRO link available in spotlight section') 
    else: 
        print('WIFI PRO link NOT available in spotlight section')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[normalize-space()='WIFI PRO']").get_attribute('href'))

def test_HMDlink(driver):

    driver.get('https://business.comcast.com/learn/phone/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@title='help me decide']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/solution-finder'

    if "https://business.comcast.com/learn/solution-finder" in element: 
        print('HELP ME DECIDE link available on page') 
    else: 
        print('HELP ME DECIDE link NOT available on on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@title='help me decide']").get_attribute('href'))  
