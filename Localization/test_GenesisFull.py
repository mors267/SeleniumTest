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

def test_Genesis(quickstart):  

    driver = quickstart
  
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
        
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("1580 OAKLAND RD STE C115 SAN JOSE CA 95131")
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="0"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/section/div/div/div[1]/div/div/form/div[2]/button').click()
    
    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Up to 300 Mbps downloads']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Shop offers page did not display!')
    time.sleep(3)

    #validate Genesis speed in speed tiers   

    #essential
    driver.get('https://business.comcast.com/shop/offers/?disablescripts=true')
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Essential']").click()
    time.sleep(1)
    timeout = 10

    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-1"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    assert element == 'Up to 100 Mbps uploads'

    #standard
    driver.find_element(by=By.XPATH, value="//li[@id='tab-2']").click()
    timeout = 10

    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-2"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    assert element == 'Up to 100 Mbps uploads'
        
    #Performance
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Performance']").click()
    timeout = 10

    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-3"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    assert element == 'Up to 200 Mbps uploads'

    #Advanced
    driver.find_element(by=By.XPATH, value="//p[normalize-space()='800 Mbps']").click()
    timeout = 10

    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-4"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    assert element == 'Up to 200 Mbps uploads'

    #Gigabit extra
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()
    timeout = 10

    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-5"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    assert element == 'Up to 300 Mbps uploads'
    
    #2 GB
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='2 Gigabit']").click()
    timeout = 10

    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-6"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    assert element == 'Up to 300 Mbps uploads'

    if "Up to 300 Mbps uploads" in element: 
        print('Genesis upload speeds displaying in offer speed tier railing') 
    else: 
        print('Genesis upload speeds NOT displaying')
        
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-6"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    print('2GB upload speed left rail: ' + element)
        
        
    # #validate Genesis text in home page  **(this section was removed June 24th 2024)**
    #
    # driver.get('https://business.comcast.com/?disablescripts=true')
    # timeout = 5
    # try:
    #     element_present = EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Introducing our fastest speed plans yet']"))
    #     WebDriverWait(driver, timeout).until(element_present)
    # except TimeoutException:
    #     print ('Home page genesis text NOT displaying')
    #
    # element = driver.find_element(by=By.XPATH, value="//h2[normalize-space()='Introducing our fastest speed plans yet']").text
    # assert element == 'Introducing our fastest speed plans yet'
    #
    # if "Introducing our fastest speed plans yet" in element: 
    #     print('Genesis text displaying in homepage') 
    # else: 
    #     print('Genesis text displaying in homepage')
    
    
    #validate Genesis upload speed in Business Internet page
    
    driver.get('https://business.comcast.com/learn/internet/business-internet?disablescripts=true')
    
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    
    #150 mbps Carousel verification
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--left > button').click()
    
    #300 mbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    
    #500 mbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    
    #800 mbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    
    #1.25 gbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    time.sleep(1)
    
    #2 gbps carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    time.sleep(1)
    
   
    #2 GBPS carousel verifcation
    driver.find_element(by=By.CSS_SELECTOR, value='#main > div.carousel.container.alj > div.slider-frame > div.carousel-arrow-container.carousel-arrow-container--right > button').click()
    time.sleep(1)
    
    element = driver.find_element(by=By.XPATH, value="//div[6]//div[1]//div[1]//div[1]//div[2]//ul[1]//li[1]//span[2]").text
    assert element == 'Up to 300 Mbps'
    
    #validate text is present on page
    if "Up to 300 Mbps" in element: 
        print('\n''Genesis upload speeds displaying on Business Internet page chart') 
    else: 
        print('\n''Genesis upload speed is NOT displaying on chart')

    element = driver.find_element(by=By.XPATH, value='//*[@id="slider"]/div[6]/div/div/div/div[2]/ul/li/span[2]').text
    print('2GB upload speed on chart: ' + element)


#health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)
