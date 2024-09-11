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

def test_ShopNowButtonHero(driver):

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@class='button']").get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    #validate correct URl is present
    if "https://business.comcast.com/shop/offers" in element: 
        print('ShopNow button available on hero') 
    else: 
        print('ShopNow button NOT available on hero')  
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@class='button']").get_attribute('href'))

    #See it in action video link

def test_SeeItInAction(driver):

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
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

def test_JumpLinks(driver):  

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
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


#Explore Speeds section

def test_ExploreSpeedsSection(driver):

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(1)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#main > div.ra-statement-container.alj-theme > div > div > div > h2').text
    assert element == 'The internet speed your business needs'

    #validate text is present on page#
    if "The internet speed your business needs" in element: 
        print('Explore Speeds section available on page') 
    else: 
        print('Explore Speeds section NOT available on page') 

    #150 mbps Carousel verification
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--left > button').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value='//*[@id="slider"]/div[1]/div/div/div/h2').text
    assert element == 'BUSINESS INTERNET ESSENTIAL'

    #validate text is present on page#
    if "BUSINESS INTERNET ESSENTIAL" in element: 
        print('Up to 150 Mbps is available on carousel') 
    else: 
        print('Up to 150 Mbps is NOT available on carousel')

    #300 mbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//strong[normalize-space()='300']").text
    assert element == '300'

    #validate text is present on page#
    if "300" in element: 
        print('Up to 300 Mbps is available on carousel') 
    else: 
        print('Up to 300 Mbps is NOT available on carousel')

    #500 mbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//strong[normalize-space()='500']").text
    assert element == '500'

    #validate text is present on page#
    if "500" in element: 
        print('Up to 500 Mbps is available on carousel') 
    else: 
        print('Up to 500 Mbps is NOT available on carousel')      

    #800 mbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//strong[normalize-space()='800']").text
    assert element == '800'

    #validate text is present on page#
    if "800" in element: 
        print('Up to 800 Mbps is available on carousel') 
    else: 
        print('Up to 800 Mbps is NOT available on carousel')

    #1.25 gbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    time.sleep(1)

    element = driver.find_element(by=By.XPATH, value="//strong[normalize-space()='1.25']").text
    assert element == '1.25'

    #validate text is present on page#
    if "1.25" in element: 
        print('Up to 1.25 gbps is available on carousel') 
    else: 
        print('Up to 1.25 gbps is NOT available on carousel')


def test_HelpMeDecidelink(driver):

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@class='button button-tertiary']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/solution-finder'

    if "https://business.comcast.com/learn/solution-finder" in element: 
        print('HELP ME DECIDE link available on page') 
    else: 
        print('HELP ME DECIDE link NOT available on page')     

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@class='button button-tertiary']").get_attribute('href'))


def test_TestMySpeedlinkValidation(driver):

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='TEST MY SPEED']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet-speed-test'

    if "https://business.comcast.com/learn/internet-speed-test" in element: 
        print('TEST MY SPEED link available on page') 
    else: 
        print('TEST MY SPEED link NOT available on page')   

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[normalize-space()='TEST MY SPEED']").get_attribute('href'))


def test_SolutionsSectionlinks(driver):
    
    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
    driver.maximize_window()

    #securityedgelink 
    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='SecurityEdge']").text
    assert element == 'SecurityEdge'

    if "SecurityEdge" in element: 
        print('SecurityEdge link available on solutions section') 
    else: 
        print('SecurityEdge link NOT available on solutions section')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[1]/a').get_attribute('href'))

    #connectionpro link
    element = driver.find_element(by=By.XPATH, value="//span[@class='cb-tile-card-title'][normalize-space()='Connection Pro']").text
    assert element == 'Connection Pro'
    
    if "Connection Pro" in element: 
        print('\n''Connection Pro link available on solutions section') 
    else: 
        print('\n''Connection Pro link NOT available on solutions section')    
    
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="solutions"]/div/div/div[2]/div/ul/li[2]/a').get_attribute('href'))
    
    
    #WiFi Pro link
    element = driver.find_element(by=By.XPATH, value="//span[@class='cb-tile-card-title'][normalize-space()='WiFi Pro']").text
    assert element == 'WiFi Pro'
        
    if "WiFi Pro" in element: 
        print('\n''WiFi Pro link available on solutions section') 
    else: 
        print('\n''WiFi Pro link NOT available on solutions section')        
    
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[27]/div/div/div[1]/div/ul/li[2]/a').get_attribute('href'))
    
    #CBM link
    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Comcast Business Mobile']").text
    assert element == 'Comcast Business Mobile'
    
    if "Comcast Business Mobile" in element: 
        print('\n''CBM link available on solutions section') 
    else: 
        print('\n''CBM link NOT available on solutions section')        
    
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[28]/div/div/div[2]/div/ul/li[2]/a').get_attribute('href'))
    
    #Ethernet link
    element = driver.find_element(by=By.XPATH, value="//span[contains(@class,'cb-tile-card-title')][normalize-space()='Ethernet Dedicated Internet']").text
    assert element == 'Ethernet Dedicated Internet'
    
    if "Ethernet Dedicated Internet" in element: 
        print('\n''Ethernet link available on solutions section') 
    else: 
        print('\n''Ethernet link NOT available on solutions section')        
    
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="ethernet"]/div/div/div[1]/div/ul/li/a').get_attribute('href'))
    

def test_ViewPlansPricingLink(driver):

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@title='VIEW PLANS AND PRICING']").get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers'

    if "https://business.comcast.com/shop/offers" in element: 
        print('VIEW PLANS AND PRICING link available on solutions section') 
    else: 
        print('VIEW PLANS AND PRICING link NOT available on solutions section')

    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@title='VIEW PLANS AND PRICING']").get_attribute('href'))

def test_ReqAQuoteLink(driver): 

    driver.get('https://business.comcast.com/learn/internet/business-internet/?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value="//button[@type='submit']").text
    assert element == 'GET STARTED'

    if "GET STARTED" in element: 
        print('Lead Gen available on page') 
    else: 
        print('Lead Gen NOT available on page') 
