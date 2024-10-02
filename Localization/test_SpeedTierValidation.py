import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

def test_SpeedTierNED(quicksetup):  

    driver = quicksetup
  
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


    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='150 Mbps']").text
    assert element == '150 Mbps'

    if "150 Mbps" in element: 
        print('Updated Speed displaying') 
    else: 
        print('Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-1"]/p').text
    print("Speed displayed in Essential Tab: " + element)

    #Standard
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Standard']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='300 Mbps']").text
    assert element == '300 Mbps'

    if "300 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-2"]/p').text
    print("Speed displayed in Standard Tab: " + element)

    #Performance
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Performance']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='500 Mbps']").text
    assert element == '500 Mbps'

    if "500 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-3"]/p').text
    print("Speed displayed in Performance Tab: " + element)

    #Advanced
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Advanced']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='800 Mbps']").text
    assert element == '800 Mbps'

    if "800 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-4"]/p').text
    print("Speed displayed in Advanced Tab: " + element)


    #Gigabit Extra
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='1.25 Gbps']").text
    assert element == '1.25 Gbps'

    if "1.25 Gbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-5"]/p').text
    print("Speed displayed in Gigabit Tab: " + element)
    
#health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)


def test_SpeedTierCEN(quicksetup):  

    driver = quicksetup
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("390 16TH AVE S STE 1 JACKSONVILLE BEACH FL 32250")
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


    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='150 Mbps']").text
    assert element == '150 Mbps'

    if "150 Mbps" in element: 
        print('Updated Speed displaying') 
    else: 
        print('Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-1"]/p').text
    print("Speed displayed in Essential Tab: " + element)

    #Standard
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Standard']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='300 Mbps']").text
    assert element == '300 Mbps'

    if "300 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-2"]/p').text
    print("Speed displayed in Standard Tab: " + element)

    #Performance
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Performance']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='500 Mbps']").text
    assert element == '500 Mbps'

    if "500 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-3"]/p').text
    print("Speed displayed in Performance Tab: " + element)

    #Advanced
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Advanced']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='800 Mbps']").text
    assert element == '800 Mbps'

    if "800 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-4"]/p').text
    print("Speed displayed in Advanced Tab: " + element)


    #Gigabit Extra
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='1.25 Gbps']").text
    assert element == '1.25 Gbps'

    if "1.25 Gbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-5"]/p').text
    print("Speed displayed in Gigabit Tab: " + element)

#health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)

def test_SpeedTierWEST(quicksetup):  

    driver = quicksetup
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("111 SW 5TH AVE STE 3700, PORTLAND OR 97204 ")
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


    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='150 Mbps']").text
    assert element == '150 Mbps'

    if "150 Mbps" in element: 
        print('Updated Speed displaying') 
    else: 
        print('Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-1"]/p').text
    print("Speed displayed in Essential Tab: " + element)

    #Standard
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Standard']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='300 Mbps']").text
    assert element == '300 Mbps'

    if "300 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-2"]/p').text
    print("Speed displayed in Standard Tab: " + element)

    #Performance
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Performance']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='500 Mbps']").text
    assert element == '500 Mbps'

    if "500 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-3"]/p').text
    print("Speed displayed in Performance Tab: " + element)

    #Advanced
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Advanced']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='800 Mbps']").text
    assert element == '800 Mbps'

    if "800 Mbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed NOT displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-4"]/p').text
    print("Speed displayed in Advanced Tab: " + element)


    #Gigabit Extra
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='1.25 Gbps']").text
    assert element == '1.25 Gbps'

    if "1.25 Gbps" in element: 
        print('\n''Updated Speed displaying') 
    else: 
        print('\n''Updated Speed displaying')

    element = driver.find_element(by=By.XPATH, value='//*[@id="tab-5"]/p').text
    print("Speed displayed in Gigabit Tab: " + element)

#health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)
