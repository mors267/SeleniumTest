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
    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()
  
    #view all offers link
  
    element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[4]/a')
    assert element.get_attribute('href') == 'https://business.comcast.com/shop/offers'
    print('ShopNow button available on hero')
    print("CTA URL:", element.get_attribute('href'))

def test_SeeItInAction(driver):
    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
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

def test_ReqAQuoteLink(driver): 

    driver.get('https://business.comcast.com/learn/internet?disablescripts=true')
    driver.maximize_window()

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value="//button[@type='submit']").text
    assert element == 'GET STARTED'

    if "GET STARTED" in element: 
        print('Lead Gen available on page') 
    else: 
        print('Lead Gen NOT available on page') 

def test_OOF(driver):

    driver.get('https://business.comcast.com/shop/gateway?disablescripts=true')
    driver.maximize_window()

    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
        
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("211 W 56TH ST FRNT 1 NEW YORK NY 10019")
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="0"]').click()
    driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
    
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='FIND A DIFFERENT PROVIDER']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Could not localize OOF address location!')
    time.sleep(3)
    
    element = driver.find_element(by=By.XPATH, value="//h2[@class='headline-4']").text
    assert element == 'Our service isn’t available at this address. You can try a different address or explore other options.'
    
    #validate correct text is present
    if "Our service isn’t available at this address. You can try a different address or explore other options." in element: 
        print('Out of Footprint messaging displaying correctly') 
    else: 
        print('Out of Footprint messaging not displaying correctly')  

