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

def test_BroadbandLabelNED(driver):  
  
    driver.maximize_window()

    driver.get('https://business.comcast.com/shop/gateway?disablescripts=true')
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("4519 main st, manchester center, VT 05255")
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="0"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/form/div[2]/button').click()

    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='300 Mbps']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Shop offers page did not display!')
    time.sleep(3)

    # check broadband label on speed tiers 

    #Essential
    driver.get('https://business.comcast.com/shop/offers/?disablescripts=true')
    time.sleep(.5)
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Essential']").click()

    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-1"]/div/div[2]/div/div[1]')
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(1.5)

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI150"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Essential, 150 Mbps/25 Mbps']").text
    assert element == 'Essential, 150 Mbps/25 Mbps'

    if "Essential, 150 Mbps/25 Mbps" in element: 
        print('Essential ingredient label displaying') 
    else: 
        print('Essential ingredient label NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="broadband-label-BI150"]/div[1]/p[1]').text
    print("Speed displayed in chart: " + element)

    #Standard
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Standard']").click()

    # element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-2"]/div/div[2]/div/div[1]')
    # driver.execute_script("return arguments[0].scrollIntoView();", element)

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI300"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')


    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Standard, 300 Mbps/35 Mbps']").text
    assert element == 'Standard, 300 Mbps/35 Mbps'

    if "Standard, 300 Mbps/35 Mbps" in element: 
        print('\n''Standard ingredient label displaying') 
    else: 
        print('\n''Standard ingredient label NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="broadband-label-BI300"]/div[1]/p[1]').text
    print("Speed displayed in chart: " + element)

    #Performance
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Performance']").click()

    # element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-3"]/div/div[2]/div/div[1]')
    # driver.execute_script("return arguments[0].scrollIntoView();", element)

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI500"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Performance, 500 Mbps/35 Mbps']").text
    assert element == 'Performance, 500 Mbps/35 Mbps'

    if "Performance, 500 Mbps/35 Mbps" in element: 
        print('\n''Performance ingredient label displaying') 
    else: 
        print('\n''Performance ingredient label NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="broadband-label-BI500"]/div[1]/p[1]').text
    print("Speed displayed in chart: " + element)

    #Advanced
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Advanced']").click()

    # element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-4"]/div/div[2]/div/div[1]')
    # driver.execute_script("return arguments[0].scrollIntoView();", element)

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI800"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Advanced, 800 Mbps/35 Mbps']").text
    assert element == 'Advanced, 800 Mbps/35 Mbps'

    if "Advanced, 800 Mbps/35 Mbps" in element: 
        print('\n''Advanced ingredient label displaying') 
    else: 
        print('\n''Advanced ingredient label NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="broadband-label-BI800"]/div[1]/p[1]').text
    print("Speed displayed in chart: " + element)


    #Gigabit Extra
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()

    # element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-6"]/div/div[2]/div/div[1]')
    # driver.execute_script("return arguments[0].scrollIntoView();", element)

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI1250"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Gigabit Extra, 1250 Mbps/35 Mbps']").text
    assert element == 'Gigabit Extra, 1250 Mbps/35 Mbps'

    if "Gigabit Extra, 1250 Mbps/35 Mbps" in element: 
        print('\n''Gigabit Extra ingredient label displaying') 
    else: 
        print('\n''Gigabit Extra ingredient label NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="broadband-label-BI1250"]/div[1]/p[1]').text
    print("Speed displayed in chart: " + element)

#health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)
