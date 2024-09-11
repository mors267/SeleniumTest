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

    driver.get('https://business.comcast.com/learn/cloud?disablescripts=true')
    driver.maximize_window()

#cloud apps jump link

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(1) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#section-1 > div.statement.cb-grid-container.container._display-left-mobile._display-center.page-chapter > div > div > h2').text
    assert element == 'Harness the power of apps and communication tools for your business'

    if "Harness the power of apps and communication tools for your business" in element: 
        print('Cloud Apps section available on page') 
    else: 
        print('Cloud Apps section NOT available on page') 

#industries jump link  

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(2) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#section-2 > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Businesses in all industries are heading to the cloud'

    if "Businesses in all industries are heading to the cloud" in element: 
        print('Industries section available on page') 
    else: 
        print('Industries section NOT available on page')

#related resources jump link 

    driver.find_element(by=By.CSS_SELECTOR, value='#main > section > div.jump-links > div > ul > li:nth-child(3) > a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#section-3 > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2').text
    assert element == 'Explore our cloud resources'

    if "Explore our cloud resources" in element: 
        print('Related Resources section available on page') 
    else: 
        print('Related Resources section NOT available on page') 

#Req a quote jump link

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.CSS_SELECTOR, value='#lead-form-container > div > legend').text
    assert element == 'Get a free quote in 2 easy steps'

    if "Get a free quote in 2 easy steps" in element: 
        print('Lead form available on page') 
    else: 
        print('Lead form NOT available on page') 


def test_CloudAppsLinks(driver):

    driver.get('https://business.comcast.com/learn/cloud?disablescripts=true')
    driver.maximize_window()

    #domain+email boxes
    element = driver.find_element(by=By.XPATH, value="//div[@class='cb-spotlights']//div[1]//div[2]//a[1]").get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email'

    if "https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email" in element: 
        print('Domain+email boxes link available in section') 
    else: 
        print('Domain+email boxes link NOT available in section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[@class='cb-spotlights']//div[1]//div[2]//a[1]").get_attribute('href')) 

    #phone add on
    element = driver.find_element(by=By.XPATH, value="//div[@id='section-1']//div//div[2]//div[2]//a[1]").get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145202/alive5-sms#!overview'

    if "https://cloudsolutions.comcast.com/apps/145202/alive5-sms#!overview" in element: 
        print('\n''Phone Add On link available in section') 
    else: 
        print('\n''Phone Add On link NOT available in section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[@id='section-1']//div//div[2]//div[2]//a[1]").get_attribute('href')) 

    #Norton security
    element = driver.find_element(by=By.XPATH, value="//div[@id='section-1']//div[3]//div[2]//a[1]").get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton'

    if "https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton" in element: 
        print('\n''Norton Security link available in section') 
    else: 
        print('\n''Norton Security link NOT available in section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[@id='section-1']//div[3]//div[2]//a[1]").get_attribute('href')) 

    #eComFax
    element = driver.find_element(by=By.XPATH, value="//div[4]//div[2]//a[1]").get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''eComFax link available in section') 
    else: 
        print('\n''eComFax link NOT available in section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[4]//div[2]//a[1]").get_attribute('href'))   

    #Microsoft Office 365
    element = driver.find_element(by=By.XPATH, value="//div[@id='section-1']//div[5]//div[2]//a[1]").get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Microsoft365 link available in section') 
    else: 
        print('\n''Microsoft365 link NOT available in section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[@id='section-1']//div[5]//div[2]//a[1]").get_attribute('href'))    

    #Headsets and webcams
    element = driver.find_element(by=By.XPATH, value="//div[6]//div[2]//a[1]").get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145074?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnHeadsets'

    if "https://cloudsolutions.comcast.com/apps/145074?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnHeadsets" in element: 
        print('\n''Headsets link available in section') 
    else: 
        print('\n''Headsets link NOT available in section')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//div[6]//div[2]//a[1]").get_attribute('href'))    


def test_ViewAllAppsLink(driver):

    driver.get('https://business.comcast.com/learn/cloud?disablescripts=true')
    driver.maximize_window()

    element = driver.find_element(by=By.XPATH, value="//a[normalize-space()='View all apps.']").get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/home?intcmp=ILC-BSEE-EXISTINGVISIT'

    if "https://cloudsolutions.comcast.com/home?intcmp=ILC-BSEE-EXISTINGVISIT" in element: 
        print('View all apps link available on page') 
    else: 
        print('View all apps link NOT available on page')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value="//a[normalize-space()='View all apps.']").get_attribute('href'))   

def test_AllDropDownLinks(driver):

    driver.get('https://business.comcast.com/learn/cloud?disablescripts=true')
    driver.maximize_window()

    #Advertising dropdown
    element = driver.find_element(by=By.CSS_SELECTOR, value='#section-2 > div.statement.cb-grid-container.container._display-left-mobile._display-center > div > div > h2')
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    time.sleep(1)

    driver.find_element(by=By.XPATH, value='//*[@data-role="accordion-trigger"]').click()

    #NetNation link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[1]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email'

    if "https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email" in element: 
        print('NetNation link available on advertising drop down') 
    else: 
        print('NetNation link NOT available on advertising drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[1]/div/div/div/div/div[1]/a').get_attribute('href'))

    #eComFax link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[1]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''eComFax link available on advertising drop down') 
    else: 
        print('eComFax link NOT available on advertising drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[1]/div/div/div/div/div[2]/a').get_attribute('href'))

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[1]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on advertising drop down') 
    else: 
        print('Office365 link NOT available on advertising drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[1]/div/div/div/div/div[3]/a').get_attribute('href'))

    #Bars and restaurants drop down

    driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[2]/h3/button').click()

    #Norton security link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[2]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton'

    if "https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton" in element: 
        print('\n''Norton Security link available on Bars and restaurants drop down') 
    else: 
        print('Norton Security link NOT available on Bars and restaurants drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[2]/div/div/div/div/div[1]/a').get_attribute('href'))

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[2]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on Bars and restaurants drop down') 
    else: 
        print('Office365 link NOT available Bars and restaurants drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[2]/div/div/div/div/div[2]/a').get_attribute('href'))   

    #NetNation link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[2]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email'

    if "https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email" in element: 
        print('\n''NetNation link available on Bars and restaurants drop down') 
    else: 
        print('NetNation link NOT available on Bars and restaurants drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[2]/div/div/div/div/div[3]/a').get_attribute('href'))

    #Contractors drop down

    driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[3]/h3/button').click()

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[3]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on Contractors drop down') 
    else: 
        print('Office365 link NOT available on Contractors drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[3]/div/div/div/div/div[1]/a').get_attribute('href'))   

    #Norton security link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[3]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton'

    if "https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton" in element: 
        print('\n''Norton security link available on Contractors drop down') 
    else: 
        print('Norton security link NOT available on Contractors drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[3]/div/div/div/div/div[3]/a').get_attribute('href'))

    #ecomfax link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[3]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''ecomfax link available on Contractors drop down') 
    else: 
        print('ecomfax link NOT available on Contractors drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[3]/div/div/div/div/div[2]/a').get_attribute('href'))

    #Financial services drop down

    driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[4]/h3/button').click()

    #ecomfax link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[4]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''ecomfax link available on Financial services drop down') 
    else: 
        print('ecomfax link NOT available on Financial services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[4]/div/div/div/div/div[1]/a').get_attribute('href'))   

    #Norton Security link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[4]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton'

    if "https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton" in element: 
        print('\n''Norton Security link available on Financial services drop down') 
    else: 
        print('Norton Security link NOT available on Financial services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[4]/div/div/div/div/div[2]/a').get_attribute('href'))

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[4]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on Financial services drop down') 
    else: 
        print('Office365 link NOT available on Financial services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[4]/div/div/div/div/div[3]/a').get_attribute('href'))

    #Health services drop down

    driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/h3/button').click()

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on health services drop down') 
    else: 
        print('Office365 link NOT available on health services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[1]/a').get_attribute('href'))   

    #ecomfax Security link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''ecomfax link available on health services drop down') 
    else: 
        print('ecomfax link NOT available on health services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[2]/a').get_attribute('href'))

    #Norton security link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton'

    if "https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton" in element: 
        print('\n''Norton security link available on health services drop down') 
    else: 
        print('Norton security link NOT available on health services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[3]/a').get_attribute('href'))

    #Insurance services drop down

    driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[6]/h3/button').click()

    #NetNation link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[6]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email'

    if "https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email" in element: 
        print('\n''NetNation link available on insurance service drop down') 
    else: 
        print('NetNation link NOT available on insurance service drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[6]/div/div/div/div/div[1]/a').get_attribute('href'))

    #ecomfax link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''ecomfax link available on Insurance services drop down') 
    else: 
        print('ecomfax link NOT available on Insurance services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[2]/a').get_attribute('href'))   

    #Norton security link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton'

    if "https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton" in element: 
        print('\n''Norton security link available on Insurance services drop down') 
    else: 
        print('Norton security link NOT available on Insurance services drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[5]/div/div/div/div/div[3]/a').get_attribute('href'))

    #Legal services drop down

    driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[7]/h3/button').click()

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[7]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on Legal drop down') 
    else: 
        print('Office365 link NOT available on Legal drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[7]/div/div/div/div/div[1]/a').get_attribute('href'))   

    #Norton security link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[7]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton'

    if "https://cloudsolutions.comcast.com/apps/144963?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnNorton" in element: 
        print('\n''Norton security link available on Legal drop down') 
    else: 
        print('Norton security link NOT available on Legal drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[7]/div/div/div/div/div[2]/a').get_attribute('href'))

    #ecomfax link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[7]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''ecomfax link available on Legal drop down') 
    else: 
        print('ecomfax link NOT available on Legal  drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[7]/div/div/div/div/div[3]/a').get_attribute('href')) 

    #Real Estate drop down

    #ecomfax link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[8]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''ecomfax link available on Real Estate drop down') 
    else: 
        print('ecomfax link NOT available on Real Estate drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[8]/div/div/div/div/div[1]/a').get_attribute('href')) 

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[8]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on Real Estate drop down') 
    else: 
        print('Office365 link NOT available on Real Estate drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[8]/div/div/div/div/div[2]/a').get_attribute('href')) 

    #NetNation link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[8]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email'

    if "https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email" in element: 
        print('\n''NetNation link available on Real Estate drop down') 
    else: 
        print('NetNation link NOT available on Real Estate drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[8]/div/div/div/div/div[3]/a').get_attribute('href'))

    #Retail drop down

    #NetNation link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[9]/div/div/div/div/div[1]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email'

    if "https://cloudsolutions.comcast.com/en-US/apps/145217/comcast-business-domain-and-email" in element: 
        print('\n''NetNation link available on retail drop down') 
    else: 
        print('NetNation link NOT available on retail drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[9]/div/div/div/div/div[1]/a').get_attribute('href'))

    #ecomfax link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[9]/div/div/div/div/div[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax'

    if "https://cloudsolutions.comcast.com/apps/144858?utm_source=myAccount&utm_medium=Referral&utm_campaign=learneComFax" in element: 
        print('\n''ecomfax link available on Retail drop down') 
    else: 
        print('ecomfax link NOT available on Retail drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[9]/div/div/div/div/div[2]/a').get_attribute('href')) 

    #Office365 link
    element = driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[9]/div/div/div/div/div[3]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365'

    if "https://cloudsolutions.comcast.com/apps/145167?utm_source=myAccount&utm_medium=Referral&utm_campaign=learnO365" in element: 
        print('\n''Office365 link available on Retail drop down') 
    else: 
        print('Office365 link NOT available on Retail drop down')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='/html/body/main/div[8]/div[2]/ul/li[9]/div/div/div/div/div[3]/a').get_attribute('href')) 
