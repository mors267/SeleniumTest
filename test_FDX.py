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

def test_FDXupload(quicksetup):
    
    driver = quicksetup
    
    timeout = 30
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ('Gateway page did not display')
    driver.find_element(by=By.XPATH, value="//input[@id='address']").click()
    driver.find_element(By.ID, "address").send_keys("5940 WATT AVE UNIT C-HMOFC NORTH HIGHLANDS CA 95660")
    time.sleep(5)
    driver.find_element(By.ID, "address").send_keys(Keys.ENTER)

    timeout = 15
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='300 Mbps']"))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Shop offers page did not display!')
    time.sleep(3)
    
    print("Upload Speeds: ")
    
    # Essential
    
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Essential']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-1"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    
    assert element == 'Up to 150 Mbps uploads', f"Essential not displaying correct upload speed: {element}"
    print("\nEssential displaying correct upload speed: " + element)
    
    #Standard
    
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Standard']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-2"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    
    assert element == 'Up to 300 Mbps uploads', f"Standard not displaying correct upload speed: {element}"
    print("Standard displaying correct upload speed: " + element)
    
    #Performance
    
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Performance']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-3"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text

    assert element == 'Up to 500 Mbps uploads', f"Performance not displaying correct upload speed: {element}"
    print("Performance displaying correct upload speed: " + element)
    
    #Advanced
    
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Advanced']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-4"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text
    
    assert element == 'Up to 800 Mbps uploads', f"Advanced not displaying correct upload speed: {element}"
    print("Advanced displaying correct upload speed: " + element)   
    
    #Gigabit Extra
    
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-5"]/div/div[1]/div[1]/div[1]/ul/li[3]/span').text

    assert element == 'Up to 1.25 Gbps uploads', f"Gigabit Extra not displaying correct upload speed: {element}"
    print("Gigabit displaying correct upload speed: " + element)
    

    # check Essentials Broadband labels
    print("\nBroadband Labels: ")
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

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Essential, 150 Mbps/150 Mbps']").text
    assert element == 'Essential, 150 Mbps/150 Mbps', f"Essential BroadBand not displaying correct download/upload speed: {element}"
    print('\n'"Essential displaying correct download/upload speed: " + element)
    
    # check Standard Broadband labels
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Standard']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-2"]/div/div[2]/div/div[1]')

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI300"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Standard, 300 Mbps/300 Mbps']").text
    
    assert element == 'Standard, 300 Mbps/300 Mbps', f"Standard BroadBand not displaying correct download/upload speed: {element}"
    print("Standard displaying correct download/upload speed: " + element)
    
    # check Performance Broadband labels
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Performance']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-3"]/div/div[2]/div/div[1]')

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI500"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Performance, 500 Mbps/500 Mbps']").text
    
    assert element == 'Performance, 500 Mbps/500 Mbps', f"Performance BroadBand not displaying correct download/upload speed: {element}"
    print("Performance displaying correct download/upload speed: " + element)
    
    # check Advanced Broadband labels
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Advanced']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-4"]/div/div[2]/div/div[1]')

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI800"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Advanced, 800 Mbps/800 Mbps']").text
    
    assert element == 'Advanced, 800 Mbps/800 Mbps', f"Advanced BroadBand not displaying correct download/upload speed: {element}"
    print("Advanced displaying correct download/upload speed: " + element)
    
    # check Gigabit Extra Broadband labels
    driver.find_element(by=By.XPATH, value="//div[normalize-space()='Gigabit Extra']").click()
    element = driver.find_element(by=By.XPATH, value='//*[@id="tabpanel-5"]/div/div[2]/div/div[1]')

    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="broadband-label-BI1250"]/div[1]/p[1]'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print ('Labels section not showing')

    element = driver.find_element(by=By.XPATH, value="//p[normalize-space()='Gigabit Extra, 1250 Mbps/1250 Mbps']").text
    
    assert element == 'Gigabit Extra, 1250 Mbps/1250 Mbps', f"Gigabit Extra BroadBand not displaying correct download/upload speed: {element}"
    print("Gigabit Extra displaying correct download/upload speed: " + element)

    #health check verification

    driver.get('https://business.comcast.com/healthcheck/')

    print('\n'"Localized to: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]').text) 
    print ("Session ID: "+driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[8]/td[2]').text)


