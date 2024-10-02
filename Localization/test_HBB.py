import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1200))  
display.start()

chromedriver_autoinstaller.install()

@pytest.fixture()    
def quicksetup(): 
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=chrome_options)
    
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    driver.get('https://business.comcast.com/shop/gateway?disablescripts=true')
    driver.maximize_window()
    driver.refresh()
    yield driver
    driver.quit() 

def test_hbbNED(quicksetup):
    
    driver = quicksetup  

    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
        
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("21627 Monmouth Ter Ashburn, VA 20147")
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="0"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/form/div[2]/button').click()
    
    timeout = 20
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Could not localize Multipicker address location!')
    time.sleep(5)
    
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/form/div/div[2]/label/span[2]').click()
    driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
    
    timeout = 20
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='GET STARTED']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Could not localize HBB address location!')
    time.sleep(5)
    
    element = driver.find_element(by=By.XPATH, value="//h2[@class='headline-4']").text
    assert element == 'Would you like to add Comcast Business service at your home address?'
    
    #validate correct text is present
    if "Would you like to add Comcast Business service at your home address?" in element: 
        print('HBB page displaying correctly')
        option1 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/div[2]/div[1]/p').text
        option2 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/div[2]/div[2]/p').text
        print("Options displayed: " + option1 + " and " + option2) 
    else: 
        print('HBB page not displaying correctly')  

def test_hbbCEN(quicksetup):
    
    driver = quicksetup  

    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("2906 BRAMBLETON PL MIDDLEBURG FL 32043")
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="0"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/form/div[2]/button').click()

    timeout = 20
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='GET STARTED']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Could not localize HBB address location!')
    time.sleep(5)
    
    element = driver.find_element(by=By.XPATH, value="//h2[@class='headline-4']").text
    assert element == 'Would you like to add Comcast Business service at your home address?'
    
    #validate correct text is present
    if "Would you like to add Comcast Business service at your home address?" in element: 
        print('HBB address displaying correctly')
        option1 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/div[2]/div[1]/p').text
        option2 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/div[2]/div[2]/p').text
        print("Options displayed: " + option1 + " and " + option2)
    else: 
        print('HBB not displaying correctly')

def test_hbbWES(quicksetup):
    
    driver = quicksetup  

    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("518 COUNCIL BLUFFS WAY VANCOUVER WA 98661")
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="0"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/form/div[2]/button').click()
    
    timeout = 20
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Could not localize Multipicker address location!')
    time.sleep(5)
    
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/form/div/div[2]/label/span[2]').click()
    driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

    timeout = 20
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='GET STARTED']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Could not localize HBB address location!')
    time.sleep(5)
    
    element = driver.find_element(by=By.XPATH, value="//h2[@class='headline-4']").text
    assert element == 'Would you like to add Comcast Business service at your home address?'
    
    #validate correct text is present
    if "Would you like to add Comcast Business service at your home address?" in element: 
        print('HBB address displaying correctly')
        option1 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/div[2]/div[1]/p').text
        option2 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/div[2]/div[2]/p').text
        print("Options displayed: " + option1 + " and " + option2)
    else: 
        print('HBB not displaying correctly')
        
    #health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)
