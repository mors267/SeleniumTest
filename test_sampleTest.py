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

def test_SIK(driver):  
    driver.get('https://business.comcast.com/shop/gateway/?disablescripts=true')
    driver.maximize_window()
    time.sleep(3)
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("3201 APOLLO DR OFC CHAMPAIGN IL 61822")
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="0"]').click()
    driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
    
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Advanced']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Could not localize in SIK enabled location!')
    time.sleep(3)
    
    # click on offer and go in buy flow
    
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()
    driver.find_element(by=By.XPATH, value="//a[@id='9326104226-primary-button']//span[@aria-hidden='true'][normalize-space()='Order Now']").click()
    
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//span[@class='s-footer-summary-drawer-item-incentive-name fs-14 _extended sik-incentive']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        element = driver.find_element(by=By.XPATH, value="//button[normalize-space()='CONTINUE']")
        driver.execute_script("return arguments[0].scrollIntoView();", element)
        time.sleep(3)
        
        driver.find_element(by=By.XPATH, value="//button[normalize-space()='CONTINUE']").click()
        time.sleep(3)

        print ('SIK not displaying in buy flow')
    
    time.sleep(3)

    #SIK validation in buy flow
    element = driver.find_element(by=By.XPATH, value="//h3[@class='cb-reveal-title']")
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(3)
            
    driver.find_element(by=By.XPATH, value="//button[normalize-space()='CONTINUE']").click()
    time.sleep(3)
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='I want the Getting Started self-installation kit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('SIK not showing in installation page')
    
    element = driver.find_element(by=By.XPATH, value="//span[normalize-space()='I want the Getting Started self-installation kit']").text
    assert element == 'I want the Getting Started self-installation kit'

    if "I want the Getting Started self-installation kit" in element: 
        print('SIK option displaying in installation page') 
    else: 
        print('SIK option NOT displaying in installation page')
    
    #continue to checkout page
    driver.find_element(by=By.XPATH, value="//button[normalize-space()='CHECKOUT']").click()
    time.sleep(3)
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Checkout page did not display')
        
    driver.find_element(By.ID, "firstName").send_keys("SIK")
    driver.find_element(By.ID, "lastName").send_keys("Test")
    driver.find_element(By.ID, "businessName").send_keys("ComcastBusinessTest")
    driver.find_element(By.ID, "telephoneNumber").send_keys("2672554566")
    driver.find_element(By.ID, "emailAddress").send_keys("testsik@test.com")

    driver.find_element(by=By.XPATH, value="//button[normalize-space()='CONTINUE']").click()
    time.sleep(3)

    element = driver.find_element(by=By.XPATH, value="//td[@class='cb-offer-summary-table-item cb-offer-summary-table-highlight--total']")
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(3)
    
    element = driver.find_element(by=By.XPATH, value="//td[normalize-space()='Self Install']").text
    assert element == 'Self Install'

    if "Self Install" in element: 
        print('SIK option displaying in Checkout page') 
    else: 
        print('SIK option NOT displaying in Checkout page')
        
#health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)
