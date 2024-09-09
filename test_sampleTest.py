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
options.add_argument("--window-size=1440, 900")


@pytest.fixture()    
def quicksetup(): 
    global driver
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome()
    driver.get('https://business.comcast.com/learn/internet/sd-wan-small-business/?disablescripts=true')
    driver.maximize_window()
    driver.refresh()
    yield driver
    driver.quit()

def test_ReqAQuoteButtonHero(quicksetup):

    driver = quicksetup

    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div/div[4]/a').get_attribute('title')
    assert element == 'REQUEST A QUOTE'
    
    #validate correct URl is present
    if "REQUEST A QUOTE" in element: 
        print('Request a Quote CTA available on hero') 
    else: 
        print('Request a Quote CTA NOT available on hero')  


def test_Features(quicksetup):

    driver = quicksetup
    
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[1]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[14]/div[1]/div/div/h2').text
    assert element == 'Secure SD-WAN. Simplified.'

    if "Secure SD-WAN. Simplified." in element: 
        print('Features section available on page') 
    else: 
        print('Features section NOT available on page')

def test_NetworkManagement(quicksetup):

    driver = quicksetup

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[2]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="network management"]/div/div/div[1]/div/h3').text
    assert element == 'Manage and monitor your network in one centralized digital portal'

    if "Manage and monitor your network in one centralized digital portal" in element: 
        print('Network Management section available on page') 
    else: 
        print('Network Management NOT available on page')
        
def test_Security(quicksetup):

    driver = quicksetup

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[3]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="security"]/div/div/div[2]/div/h3').text
    assert element == 'Security for peace of mind'

    if "Security for peace of mind" in element: 
        print('Security section available on page') 
    else: 
        print('Security NOT available on page')
        
    # learn more CTA
        
    learn_more_locator = '//*[@id="security"]/div/div/div[2]/div/a'
    learn_more_elm = driver.find_element(By.XPATH, learn_more_locator)
    learn_more_elm.click()
    
    cur_url = driver.current_url
    expected_url = 'https://business.comcast.com/enterprise/products-services/cybersecurity-services/advanced-security'
    
    assert cur_url == expected_url, f"Expected URL: {expected_url}, but got: {driver.current_url}"
    print("Learn More link redirects to the correct URL.")
    
def test_SmallBusinessSolution(quicksetup):

    driver = quicksetup

    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[4]/a').click()
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="solution"]/div[1]/div/div/h2').text
    assert element == 'The network solution your small business needs'

    if "The network solution your small business needs" in element: 
        print('Small business solution section available on page') 
    else: 
        print('Small business solution section NOT available on page')
        
    # connect with an agent link
        
    connect_agent = '//*[@id="solution"]/div[2]/table/tbody/tr[6]/td/ul/li/a'
    connect_agent_elm = driver.find_element(By.XPATH, connect_agent)
    connect_agent_elm.click()
    
    cur_url = driver.current_url
    expected_url = 'https://business.comcast.com/contact'
    
    assert cur_url == expected_url, f"Expected URL: {expected_url}, but got: {driver.current_url}"
    print("Connect with an agent link redirects to the correct URL.")

def test_Insights(quicksetup):
    driver = quicksetup

    # Click the "Insights" section
    driver.find_element(By.XPATH, '//*[@id="main"]/section/div[2]/div/ul/li[5]/a').click()
    time.sleep(2)

    # Verify the header in the "Insights" section
    element = driver.find_element(By.XPATH, '//*[@id="insights"]/div[1]/div/div/h2').text
    assert element == 'Industry insights', f"Expected 'Industry insights', but got '{element}'"

    if "Industry insights" in element:
        print('Industry insights section available on page')
    else:
        print('Industry insights section NOT available on page')

    # First article redirect
    first_article = '//*[@id="insights"]/div[2]/div[1]/div/a'
    driver.find_element(By.XPATH, first_article).click()

    # Switch to the new tab
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])

    cur_url = driver.current_url
    expected_url = 'https://business.comcast.com/community/browse-all/details/from-single-location-businesses-to-enterprise-branch-of-one-how-sd-wan-is-evolving-to-address-more-needs'

    assert cur_url == expected_url, f"Expected URL: {expected_url}, but got: {cur_url}"
    print("First article link redirects to the correct URL.")

    # Close the current tab and switch back to the original
    driver.close()
    driver.switch_to.window(window_handles[0])
    time.sleep(2)

    # Second article redirect
    second_article = '//*[@id="insights"]/div[2]/div[2]/div/a'
    driver.find_element(By.XPATH, second_article).click()

    # Switch to the new tab
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])

    cur_url = driver.current_url
    expected_url = 'https://business.comcast.com/community/browse-all/details/sd-wan-for-small-midsize-and-franchise-businesses-standalone-and-cloud-first-solutions'

    assert cur_url == expected_url, f"Expected URL: {expected_url}, but got: {cur_url}"
    print("Second article link redirects to the correct URL.")

    # Close the current tab and switch back to the original
    driver.close()
    driver.switch_to.window(window_handles[0])
    time.sleep(2)

    # Third article redirect
    third_article = '//*[@id="insights"]/div[2]/div[3]/div/a'
    driver.find_element(By.XPATH, third_article).click()

    # Switch to the new tab
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])

    cur_url = driver.current_url
    expected_url = 'https://business.comcast.com/community/browse-all/details/use-sd-wan-if-you-re-doing-any-of-these-five-things'

    assert cur_url == expected_url, f"Expected URL: {expected_url}, but got: {cur_url}"
    print("Third article link redirects to the correct URL.")

    # Close the current tab and switch back to the original
    driver.close()
    driver.switch_to.window(window_handles[0])
    time.sleep(2)

                             
def test_ReqAQuoteJumpLink(quicksetup):                                                                                     
                                                 
    driver = quicksetup
    
    driver.find_element(by=By.XPATH, value='//*[@id="main"]/section/div[2]/div/ul/li[6]/a').click()       
    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value='//*[@id="lead-form-container"]/div/legend').text
    assert element == 'Request a sales consultation'
              
    if "Request a sales consultation" in element: 
        print('Lead Form section available on page') 
    else: 
        print('Lead Form section NOT available on page') 

