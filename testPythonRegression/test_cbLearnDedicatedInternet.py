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

    driver.get('https://business.comcast.com/learn/internet/dedicated-internet/?disablescripts=true')
    driver.maximize_window()

#UnderstandingEthernet jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="features"]/div[1]/div/div/h2').text
    assert element == 'Why Ethernet Dedicated Internet?'

    if "Why Ethernet Dedicated Internet?" in element: 
        print('Ethernet section available on page') 
    else: 
        print('Ethernet section NOT available on page') 

#Features jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="understanding"]/div/div[1]/div[3]/h3').text
    assert element == 'BGP routing'

    element = driver.find_element(by=By.XPATH, value='//*[@id="understanding"]/div/div[2]/div[3]/h3').text
    assert element == 'Static IP addresses'

    if "BGP routing" and "Static IP addresses" in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page')

#PuttingEDI to work jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="ideal"]/div[1]/div/div/h2').text
    assert element == 'Putting Ethernet Dedicated Internet to work'

    if "Putting Ethernet Dedicated Internet to work" in element: 
        print('EDI section available on page') 
    else: 
        print('EDI section NOT available on page')       

#solutions jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/h3').text
    assert element == 'Collaboration technologies that keep up with demand'

    if "Collaboration technologies that keep up with demand" in element: 
        print('Solutions section available on page') 
    else: 
        print('Solutions section NOT available on page')

#Req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[5]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page') 


def test_RequestAQuoteHero(driver): 

    driver.get('https://business.comcast.com/learn/internet/dedicated-internet/?disablescripts=true')
    driver.maximize_window()

    #validate Home page Hero POI Modal is present on page#
    element = driver.find_element(by=By.XPATH, value="//a[@title='REQUEST A QUOTE']").text
    assert element == 'REQUEST A QUOTE'

    if "REQUEST A QUOTE" in element: 
        print('REQUEST A QUOTE link available on homepage hero') 
    else: 
        print('REQUEST A QUOTE link NOT available on homepage hero')

    driver.find_element(by=By.XPATH, value="//a[@title='REQUEST A QUOTE']").click()
    time.sleep(1)


def test_ValidateSolutionsSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/internet/dedicated-internet/?disablescripts=true')
    driver.maximize_window()

#VoiceEdge link

    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='VoiceEdge']").text
    assert element == 'VoiceEdge'

    if "VoiceEdge" in element: 
        print('VoiceEdge link available on page') 
    else: 
        print('VoiceEdge link NOT available on page')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[1]/a').get_attribute('href'))

#PRI trunks link

    element = driver.find_element(by=By.XPATH, value="//span[@class='cb-tile-card-title'][normalize-space()='PRI Trunks']").text
    assert element == 'PRI Trunks'

    if "PRI Trunks" in element: 
        print('\n''PRI Trunks link available on page') 
    else: 
        print('\n''PRI Trunks link NOT available on page')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))     

#SIP trunks link

    element = driver.find_element(by=By.XPATH, value="//span[@class='cb-tile-card-title'][normalize-space()='SIP Trunks']").text
    assert element == 'SIP Trunks'

    if "SIP Trunks" in element: 
        print('\n''SIP Trunks link available on page') 
    else: 
        print('\n''SIP Trunks link NOT available on page')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[1]/div/ul/li[3]/a').get_attribute('href'))     

