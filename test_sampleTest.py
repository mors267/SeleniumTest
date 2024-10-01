from selenium import webdriver 
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture()    
def quicksetup(): 
    global driver
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-proxy-server")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome()
    driver.get('https://business.comcast.com/shop/gateway?disablescripts=true')
    driver.maximize_window()
    driver.refresh()
    yield driver
    driver.quit() 

def test_OOF(quicksetup):
    
    driver = quicksetup  

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
    
    timeout = 60
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
        

    
