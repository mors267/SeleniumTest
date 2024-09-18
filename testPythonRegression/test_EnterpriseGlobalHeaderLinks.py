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
  
def test_EnterpriseSolutionsDropDownLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #Global secure networking solutions
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-meganav-panel-Enterprise Solutions"]/section/div[1]/a[1]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/secure-network-solutions'

    if "https://business.comcast.com/enterprise/products-services/secure-network-solutions" in element: 
        print('Global Secure Networking Solutions link available in Enterprise global header') 
    else: 
        print('Global Secure Networking Solutions link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-meganav-panel-Enterprise Solutions"]/section/div[1]/a[1]').get_attribute('href'))

    #Product offering link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-meganav-panel-Enterprise Solutions"]/section/div[1]/a[2]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services'

    if "https://business.comcast.com/enterprise/products-services" in element: 
        print('\n''Product offerings link available in Enterprise global header') 
    else: 
        print('Product offerings link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-meganav-panel-Enterprise Solutions"]/section/div[1]/a[2]').get_attribute('href'))  

    #Req consultation link
    element = driver.find_element(by=By.XPATH, value='//*[@id="request-a-consultation-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/request-consultation'

    if "https://business.comcast.com/enterprise/request-consultation" in element: 
        print('\n''request-a-consultation link available in Enterprise global header') 
    else: 
        print('request-a-consultation link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="request-a-consultation-header-id"]').get_attribute('href'))  

    #Executive briefing link
    element = driver.find_element(by=By.XPATH, value='//*[@id="executive-briefing-centers-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/executive-briefing-center'

    if "https://business.comcast.com/enterprise/executive-briefing-center" in element: 
        print('\n''executive-briefing link available in Enterprise global header') 
    else: 
        print('executive-briefing link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="executive-briefing-centers-header-id"]').get_attribute('href'))  

    #Events link
    element = driver.find_element(by=By.XPATH, value='//*[@id="events-header-id"]').get_attribute('href')
    assert element == 'https://comcastbusinessevents.comcast.com/'

    if "https://comcastbusinessevents.comcast.com/" in element: 
        print('\n''events link available in Enterprise global header') 
    else: 
        print('events link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="events-header-id"]').get_attribute('href'))  

    #Contact ent support link
    element = driver.find_element(by=By.XPATH, value='//*[@id="contact-enterprise-support-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/enterprise-support'

    if "https://business.comcast.com/enterprise/enterprise-support" in element: 
        print('\n''contact-enterprise-support link available in Enterprise global header') 
    else: 
        print('contact-enterprise-support link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="contact-enterprise-support-header-id"]').get_attribute('href'))  

    #PGA link
    element = driver.find_element(by=By.XPATH, value='//*[@id="pga-tour-partnership-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/pga-tour'

    if "https://business.comcast.com/pga-tour" in element: 
        print('\n''PGA link available in Enterprise global header') 
    else: 
        print('PGA link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="pga-tour-partnership-header-id"]').get_attribute('href'))  
    

def test_EnterpriseSDWanSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #SD WAN solutions section
    element = driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/sd-wan-solutions'

    if "https://business.comcast.com/enterprise/products-services/sd-wan-solutions" in element: 
        print('SD Wan Solutions link available in Enterprise global header') 
    else: 
        print('SD Wan Solutions link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-header-id"]').get_attribute('href'))

    #SD WAN 
    element = driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/sd-wan-solutions/sd-wan'

    if "https://business.comcast.com/enterprise/products-services/sd-wan-solutions/sd-wan" in element: 
        print('\n''SD Wan link available in Enterprise global header') 
    else: 
        print('\n''SD Wan link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-list-id"]/li[1]/a').get_attribute('href'))

    #Managed router firewall
    element = driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/sd-wan-solutions/managed-router-firewall'

    if "https://business.comcast.com/enterprise/products-services/sd-wan-solutions/managed-router-firewall" in element: 
        print('\n''Managed router firewall link available in Enterprise global header') 
    else: 
        print('\n''Managed router firewall NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-list-id"]/li[2]/a').get_attribute('href'))
    
    #Activecore 
    element = driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/sd-wan-solutions/activecore-digital-experience'

    if "https://business.comcast.com/enterprise/products-services/sd-wan-solutions/activecore-digital-experience" in element: 
        print('\n''ActiveCore link available in Enterprise global header') 
    else: 
        print('\n''ActiveCore NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="sd-wan-solutions-list-id"]/li[3]/a').get_attribute('href'))


def test_EnterpriseDataNetworkingSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #datanetworking link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking'

    if "https://business.comcast.com/enterprise/products-services/data-networking" in element: 
        print('Data networking link available in Enterprise global header') 
    else: 
        print('Data networking link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-header-id"]').get_attribute('href'))

    #Ethernet network services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking/ethernet-network-services'

    if "https://business.comcast.com/enterprise/products-services/data-networking/ethernet-network-services" in element: 
        print('\n''Ethernet network services link available in Enterprise global header') 
    else: 
        print('\n''Ethernet network services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[1]/a').get_attribute('href'))
 
    #Ethernet dedicated internet link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking/ethernet-dedicated-internet'

    if "https://business.comcast.com/enterprise/products-services/data-networking/ethernet-dedicated-internet" in element: 
        print('\n''Ethernet dedicated internet link available in Enterprise global header') 
    else: 
        print('\n''Ethernet dedicated internet link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[2]/a').get_attribute('href'))         

    #Ethernet private line link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking/ethernet-private-line'

    if "https://business.comcast.com/enterprise/products-services/data-networking/ethernet-private-line" in element: 
        print('\n''Ethernet private line link available in Enterprise global header') 
    else: 
        print('\n''Ethernet private line link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[3]/a').get_attribute('href'))     

    #Ethernet virtual private line link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking/ethernet-virtual-private-line'

    if "https://business.comcast.com/enterprise/products-services/data-networking/ethernet-virtual-private-line" in element: 
        print('\n''Ethernet virtual private line link available in Enterprise global header') 
    else: 
        print('\n''Ethernet virtual private line link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[4]/a').get_attribute('href')) 
    
    #Business internet link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking/business-internet'

    if "https://business.comcast.com/enterprise/products-services/data-networking/business-internet" in element: 
        print('\n''Business internet link available in Enterprise global header') 
    else: 
        print('\n''Business internet link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[5]/a').get_attribute('href')) 
    
    #Cell backhaul link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking/cell-backhaul'

    if "https://business.comcast.com/enterprise/products-services/data-networking/cell-backhaul" in element: 
        print('\n''Cell backhaul link available in Enterprise global header') 
    else: 
        print('\n''Cell backhaul link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[6]/a').get_attribute('href')) 
    
    #Wavelength Services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[7]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/data-networking/wavelengths'

    if "https://business.comcast.com/enterprise/products-services/data-networking/wavelengths" in element: 
        print('\n''Wavelength link available in Enterprise global header') 
    else: 
        print('\n''Wavelength link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="data-networking-list-id"]/li[7]/a').get_attribute('href')) 

def test_EnterpriseCyberSecuritySectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #Cybersecutiy Services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cybersecurity-services'

    if "https://business.comcast.com/enterprise/products-services/cybersecurity-services" in element: 
        print('Cybersecutiy services link available in Enterprise global header') 
    else: 
        print('Cybersecutiy services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-header-id"]').get_attribute('href')) 

    #Advanced security link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cybersecurity-services/advanced-security'

    if "https://business.comcast.com/enterprise/products-services/cybersecurity-services/advanced-security" in element: 
        print('\n''Advanced security link available in Enterprise global header') 
    else: 
        print('\n''Advanced security  link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[1]/a').get_attribute('href')) 

    #Ddos link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cybersecurity-services/ddos-threat-mitigation'

    if "https://business.comcast.com/enterprise/products-services/cybersecurity-services/ddos-threat-mitigation" in element: 
        print('\n''Ddos mitigation link available in Enterprise global header') 
    else: 
        print('\n''Ddos mitigation link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[2]/a').get_attribute('href'))
    
    #Advanced Detection and Response link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cybersecurity-services/managed-detection-and-response'

    if "https://business.comcast.com/enterprise/products-services/cybersecurity-services/managed-detection-and-response" in element: 
        print('\n''Advanced Detection link available in Enterprise global header') 
    else: 
        print('\n''Advanced Detection link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[3]/a').get_attribute('href'))  

    #managed security edge link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/managed-security'

    if "https://business.comcast.com/enterprise/products-services/managed-services/managed-security" in element: 
        print('\n''Managed security link available in Enterprise global header') 
    else: 
        print('\n''Managed security link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[4]/a').get_attribute('href')) 

    #securityedge edge link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cybersecurity-services/comcast-business-securityedge'

    if "https://business.comcast.com/enterprise/products-services/cybersecurity-services/comcast-business-securityedge" in element: 
        print('\n''SecurityEdge link available in Enterprise global header') 
    else: 
        print('\n''SecurityEdge link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cybersecurity-services-list-id"]/li[5]/a').get_attribute('href')) 


def test_EnterpriseUnifiedCommunicationSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #Unified Communications link
    element = driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/unified-communications'

    if "https://business.comcast.com/enterprise/products-services/unified-communications" in element: 
        print('Unified Communications link available in Enterprise global header') 
    else: 
        print('Unified Communications link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-header-id"]').get_attribute('href')) 

    #Business voiceedge link
    element = driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/unified-communications/comcast-business-voiceedge'

    if "https://business.comcast.com/enterprise/products-services/unified-communications/comcast-business-voiceedge" in element: 
        print('\n''Business VoiceEdge link available in Enterprise global header') 
    else: 
        print('\n''Business VoiceEdge link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-list-id"]/li[1]/a').get_attribute('href')) 

    #SIP trunks link
    element = driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/unified-communications/sip-trunks'

    if "https://business.comcast.com/enterprise/products-services/unified-communications/sip-trunks" in element: 
        print('\n''SIP trunks link available in Enterprise global header') 
    else: 
        print('\n''SIP trunks link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-list-id"]/li[2]/a').get_attribute('href')) 

    #PRI trunks link
    element = driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/unified-communications/isdn-pri'

    if "https://business.comcast.com/enterprise/products-services/unified-communications/isdn-pri" in element: 
        print('\n''PRI trunks link available in Enterprise global header') 
    else: 
        print('\n''PRI trunks link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="unified-communications-list-id"]/li[3]/a').get_attribute('href')) 

def test_EnterpriseCloudSolutionsSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #cloud solutions link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cloud-solutions'

    if "https://business.comcast.com/enterprise/products-services/cloud-solutions" in element: 
        print('cloud solutions link available in Enterprise global header') 
    else: 
        print('cloud solutions link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-header-id"]').get_attribute('href'))

    #AWS services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cloud-solutions/amazon-web-services'

    if "https://business.comcast.com/enterprise/products-services/cloud-solutions/amazon-web-services" in element: 
        print('\n''AWS services link available in Enterprise global header') 
    else: 
        print('\n''AWS services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-list-id"]/li[1]/a').get_attribute('href'))
    
    #Azure services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cloud-solutions/microsoft-azure'

    if "https://business.comcast.com/enterprise/products-services/cloud-solutions/microsoft-azure" in element: 
        print('\n''Azure services link available in Enterprise global header') 
    else: 
        print('\n''Azure services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-list-id"]/li[2]/a').get_attribute('href'))
    
    #IBM cloud services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/cloud-solutions/ibm-cloud'

    if "https://business.comcast.com/enterprise/products-services/cloud-solutions/ibm-cloud" in element: 
        print('\n''IBM cloud services link available in Enterprise global header') 
    else: 
        print('\n''IBM cloud services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="cloud-solutions-list-id"]/li[3]/a').get_attribute('href'))
    
def test_EnterpriseBusTVServicesSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #Business tv services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/business-tv-solutions'

    if "https://business.comcast.com/enterprise/products-services/business-tv-solutions" in element: 
        print('Business TV services link available in Enterprise global header') 
    else: 
        print('Business TV services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-header-id"]').get_attribute('href'))

    #X1 Bars and restaurants link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/business-tv-solutions/x1-bars-restaurants'

    if "https://business.comcast.com/enterprise/products-services/business-tv-solutions/x1-bars-restaurants" in element: 
        print('\n''X1 Bars and restaurants link available in Enterprise global header') 
    else: 
        print('\n''X1 Bars and restaurants link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-list-id"]/li[1]/a').get_attribute('href'))

    #X1 hospitality link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/business-tv-solutions/x1-hospitality'

    if "https://business.comcast.com/enterprise/products-services/business-tv-solutions/x1-hospitality" in element: 
        print('\n''X1 hospitality link available in Enterprise global header') 
    else: 
        print('\n''X1 hospitality link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-list-id"]/li[2]/a').get_attribute('href'))
    
    #X1 offices link
    element = driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/business-tv-solutions/offices'

    if "https://business.comcast.com/enterprise/products-services/business-tv-solutions/offices" in element: 
        print('\n''X1 offices link available in Enterprise global header') 
    else: 
        print('\n''X1 offices link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="business-tv-services-list-id"]/li[3]/a').get_attribute('href'))
    
    
def test_EnterpriseManagedSolutionsSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #Managed solutions services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services'

    if "https://business.comcast.com/enterprise/products-services/managed-services" in element: 
        print('Managed solutions services link available in Enterprise global header') 
    else: 
        print('Managed solutions services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-header-id"]').get_attribute('href'))

    #Connectivity link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/managed-connectivity'

    if "https://business.comcast.com/enterprise/products-services/managed-services/managed-connectivity" in element: 
        print('\n''Connectivity link available in Enterprise global header') 
    else: 
        print('\n''Connectivity link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[1]/a').get_attribute('href'))

    #WIFI analytics link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/managed-wifi'

    if "https://business.comcast.com/enterprise/products-services/managed-services/managed-wifi" in element: 
        print('\n''Wifi analytics link available in Enterprise global header') 
    else: 
        print('\n''Wifi analytics link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[2]/a').get_attribute('href'))
    
    #Routers link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/managed-router'

    if "https://business.comcast.com/enterprise/products-services/managed-services/managed-router" in element: 
        print('\n''Routers link available in Enterprise global header') 
    else: 
        print('\n''Routers link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[3]/a').get_attribute('href'))
    
    #security link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/managed-security'

    if "https://business.comcast.com/enterprise/products-services/managed-services/managed-security" in element: 
        print('\n''security link available in Enterprise global header') 
    else: 
        print('\n''security link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[4]/a').get_attribute('href'))
    
    #Voice link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/managed-voice'

    if "https://business.comcast.com/enterprise/products-services/managed-services/managed-voice" in element: 
        print('\n''Voice link available in Enterprise global header') 
    else: 
        print('\n''Voice link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[5]/a').get_attribute('href'))
    
    #business continuity link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/managed-business-continuity'

    if "https://business.comcast.com/enterprise/products-services/managed-services/managed-business-continuity" in element: 
        print('\n''business continuity link available in Enterprise global header') 
    else: 
        print('\n''business continuity link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[6]/a').get_attribute('href'))

    #IT deployment link
    element = driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[7]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/products-services/managed-services/it-deployment-services'

    if "https://business.comcast.com/enterprise/products-services/managed-services/it-deployment-services" in element: 
        print('\n''IT deployment link available in Enterprise global header') 
    else: 
        print('\n''IT deployment link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="managed-solutions-list-id"]/li[7]/a').get_attribute('href'))
    
def test_EnterpriseIndustrySolutionsSectionLinks(driver):

    driver.get('https://business.comcast.com/learn/tv/bars-restaurants/?disablescripts=true')
    driver.maximize_window()

    #Industry solutions link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions'

    if "https://business.comcast.com/enterprise/industry-solutions" in element: 
        print('Industry solutions link available in Enterprise global header') 
    else: 
        print('Industry solutions link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-header-id"]').get_attribute('href'))

    #Retail link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/retail'

    if "https://business.comcast.com/enterprise/industry-solutions/retail" in element: 
        print('\n''Retail link available in Enterprise global header') 
    else: 
        print('\n''Retail link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[1]/a').get_attribute('href'))

    #Financial services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/financial-services'

    if "https://business.comcast.com/enterprise/industry-solutions/financial-services" in element: 
        print('\n''Financial services link available in Enterprise global header') 
    else: 
        print('\n''Financial services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[2]/a').get_attribute('href'))
    
    #Restaurants and Food Services link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/restaurants-food-services'

    if "https://business.comcast.com/enterprise/industry-solutions/restaurants-food-services" in element: 
        print('\n''Restaurants and Food Services link available in Enterprise global header') 
    else: 
        print('\n''Restaurants and Food Services link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[3]/a').get_attribute('href'))
    
    #Hospitality link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/hospitality'

    if "https://business.comcast.com/enterprise/industry-solutions/hospitality" in element: 
        print('\n''Hospitality link available in Enterprise global header') 
    else: 
        print('\n''Hospitality link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[4]/a').get_attribute('href'))
    
    #Healthcare link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/healthcare'

    if "https://business.comcast.com/enterprise/industry-solutions/healthcare" in element: 
        print('\n''Healthcare link available in Enterprise global header') 
    else: 
        print('\n''Healthcare link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[5]/a').get_attribute('href'))
    
    #Education link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/education'

    if "https://business.comcast.com/enterprise/industry-solutions/education" in element: 
        print('\n''Education link available in Enterprise global header') 
    else: 
        print('\n''Education link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[6]/a').get_attribute('href'))

    #Federal Government link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[7]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/federal-government'

    if "https://business.comcast.com/enterprise/industry-solutions/federal-government" in element: 
        print('\n''Federal Government link available in Enterprise global header') 
    else: 
        print('\n''Federal Government link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[7]/a').get_attribute('href'))
    
    #State and Local Government link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[8]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/state-local-government'

    if "https://business.comcast.com/enterprise/industry-solutions/state-local-government" in element: 
        print('\n''State and Local Government link available in Enterprise global header') 
    else: 
        print('\n''State and Local Government link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[8]/a').get_attribute('href'))

    #Manufacturing link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[9]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/manufacturing'

    if "https://business.comcast.com/enterprise/industry-solutions/manufacturing" in element: 
        print('\n''Manufacturing link available in Enterprise global header') 
    else: 
        print('\n''Manufacturing link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[9]/a').get_attribute('href'))
    
    #Property Development link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[10]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/property-development'

    if "https://business.comcast.com/enterprise/industry-solutions/property-development" in element: 
        print('\n''Property Development link available in Enterprise global header') 
    else: 
        print('\n''Property Development link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[10]/a').get_attribute('href'))
    
    #Stadiums link
    element = driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[11]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/industry-solutions/stadiums'

    if "https://business.comcast.com/enterprise/industry-solutions/stadiums" in element: 
        print('\n''Stadiums link available in Enterprise global header') 
    else: 
        print('\n''Stadiums link NOT available in Enterprise global header')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="industry-solutions-list-id"]/li[11]/a').get_attribute('href'))
        
