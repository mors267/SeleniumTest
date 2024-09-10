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
    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()
    driver.refresh()

    #view all offers link
  
    element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[4]/a')
    assert element.get_attribute('href') == 'https://business.comcast.com/shop/offers'
    print('Pass')
    print("CTA URL:", element.get_attribute('href'))

def test_SeeItInAction(driver):

    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()
    driver.refresh()

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

    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()
    driver.refresh()

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
