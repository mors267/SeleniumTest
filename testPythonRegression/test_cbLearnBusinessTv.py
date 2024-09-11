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

    driver.get('https://business.comcast.com/learn/tv/?disablescripts=true')
    driver.maximize_window()

#Public view tv jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="public"]/div/div/div[2]/div/p').text
    assert element == 'PUBLIC VIEWING TV'

    if "PUBLIC VIEWING TV" in element: 
        print('Public view tv section available on page') 
    else: 
        print('Public view tv section NOT available on page')

    element = driver.find_element(by=By.XPATH, value='//*[@id="public"]/div/div/div[2]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/public'

    if "https://business.comcast.com/learn/tv/public" in element: 
        print('Public viewing tv link available on section') 
    else: 
        print('Public viewing tv link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="public"]/div/div/div[2]/div/ul/li/a').get_attribute('href'))

#Bar and Restaurant TV jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="bar"]/div/div/div[1]/div/p').text
    assert element == 'BAR AND RESTAURANT TV'

    if "BAR AND RESTAURANT TV" in element: 
        print('\n''Bar and Restaurant TV section available on page') 
    else: 
        print('\n''Bar and Restaurant TV  NOT available on page')

    element = driver.find_element(by=By.XPATH, value='//*[@id="bar"]/div/div/div[1]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/bars-restaurants'

    if "https://business.comcast.com/learn/tv/bars-restaurants" in element: 
        print('Bar and Restaurant tv link available on section') 
    else: 
        print('Bar and Restaurant tv link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bar"]/div/div/div[1]/div/ul/li/a').get_attribute('href')) 

#Private view tv jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="private"]/div/div/div[2]/div/p').text
    assert element == 'PRIVATE VIEWING TV'

    if "PRIVATE VIEWING TV" in element: 
        print('\n''Private View TV section available on page') 
    else: 
        print('\n''Private View TV NOT available on page')

    element = driver.find_element(by=By.XPATH, value='//*[@id="private"]/div/div/div[2]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/private'

    if "https://business.comcast.com/learn/tv/private" in element: 
        print('Private view link available on section') 
    else: 
        print('Private view tv link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="private"]/div/div/div[2]/div/ul/li/a').get_attribute('href'))   

#In room ent jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="in-room"]/div/div/div[1]/div/p').text
    assert element == 'IN-ROOM ENTERTAINMENT'

    if "IN-ROOM ENTERTAINMENT" in element: 
        print('\n''IN-ROOM ENTERTAINMENT section available on page') 
    else: 
        print('\n''IN-ROOM ENTERTAINMENT section NOT available on page')

    element = driver.find_element(by=By.XPATH, value='//*[@id="in-room"]/div/div/div[1]/div/ul/li/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/hotels'

    if "https://business.comcast.com/learn/tv/hotels" in element: 
        print('X1 for hospitality link available on section') 
    else: 
        print('X1 for hospitality tv link NOT available on section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="private"]/div/div/div[2]/div/ul/li/a').get_attribute('href'))           

#req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[5]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('\n''Lead Form section available on page') 
    else: 
        print('\n''Lead Form section NOT available on page') 

def test_ViewChannelLineupCTA(driver):

    driver.get('https://business.comcast.com/learn/tv/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='VIEW CHANNEL LINEUP']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv/channel-lineup'

    if "https://business.comcast.com/learn/tv/channel-lineup" in element: 
        print('View channel lineup link available on page') 
    else: 
        print('View channel lineup link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[normalize-space()='VIEW CHANNEL LINEUP']").get_attribute('href'))

def test_HMDlink(driver):

    driver.get('https://business.comcast.com/learn/tv/?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[@class='button button-tertiary']").get_attribute('href')
    assert element == 'https://business.comcast.com/learn/solution-finder'

    if "https://business.comcast.com/learn/solution-finder" in element: 
        print('HMD link available on page') 
    else: 
        print('HMD link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[@class='button button-tertiary']").get_attribute('href'))   
