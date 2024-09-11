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

def test_ShopFooterLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

#view all offers link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-footer-wrapper"]/div[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/'

    if "https://business.comcast.com/" in element: 
        print('CBM logo home page link available in global footer') 
    else: 
        print('CBM logo home page link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-footer-wrapper"]/div[1]/a').get_attribute('href'))

    #Shop link
    element = driver.find_element(by=By.XPATH, value='//*[@id="shop-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/'

    if "https://business.comcast.com/" in element: 
        print('\n''Shop link available in global footer') 
    else: 
        print('Shop link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="shop-header-id"]').get_attribute('href'))  

    #PlanPricing link
    element = driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/shop/offers?services=All&internetdownloadspeed=All&contractlength=All&price=All'

    if "https://business.comcast.com/shop/offers?services=All&internetdownloadspeed=All&contractlength=All&price=All" in element: 
        print('\n''Plan and Pricing link available in global footer') 
    else: 
        print('Plan and Pricing link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[1]/a').get_attribute('href')) 

    #Internet link
    element = driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/internet'

    if "https://business.comcast.com/learn/internet" in element: 
        print('\n''Internet link available in global footer') 
    else: 
        print('Internet link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[2]/a').get_attribute('href')) 

    #Mobile link
    element = driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/mobile'

    if "https://business.comcast.com/learn/mobile" in element: 
        print('\n''Mobile link available in global footer') 
    else: 
        print('Mobile link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[3]/a').get_attribute('href')) 

    #Phone link
    element = driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/phone'

    if "https://business.comcast.com/learn/phone" in element: 
        print('\n''Phone link available in global footer') 
    else: 
        print('Phone link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[4]/a').get_attribute('href')) 

    #BusinessTV link
    element = driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/tv'

    if "https://business.comcast.com/learn/tv" in element: 
        print('\n''Business TV link available in global footer') 
    else: 
        print('Business TV link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[5]/a').get_attribute('href'))    

    #CloudApps link
    element = driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/learn/cloud'

    if "https://business.comcast.com/learn/cloud" in element: 
        print('\n''Cloud Apps link available in global footer') 
    else: 
        print('Cloud Apps link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="shop-list-id"]/li[6]/a').get_attribute('href'))
    
def test_SupportFooterLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #Support link
    element = driver.find_element(by=By.XPATH, value='//*[@id="support-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/support/home/'

    if "https://business.comcast.com/support/home/" in element: 
        print('Support link available in global footer') 
    else: 
        print('Support link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="support-header-id"]').get_attribute('href'))

    #CB Support link
    element = driver.find_element(by=By.XPATH, value='//*[@id="support-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/support/home/'

    if "https://business.comcast.com/support/home/" in element: 
        print('\n''CB Support link available in global footer') 
    else: 
        print('CB Support link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="support-list-id"]/li[1]/a').get_attribute('href'))

    #Forums link
    element = driver.find_element(by=By.XPATH, value='//*[@id="support-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://forums.businesshelp.comcast.com/'

    if "https://forums.businesshelp.comcast.com/" in element: 
        print('\n''Forums link available in global footer') 
    else: 
        print('Forums link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="support-list-id"]/li[2]/a').get_attribute('href'))

    #Find Xfinity Store link
    element = driver.find_element(by=By.XPATH, value='//*[@id="support-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://www.xfinity.com/local/store-offers'

    if "https://www.xfinity.com/local/store-offers" in element: 
        print('\n''Find Xfinity Store link available in global footer') 
    else: 
        print('Find Xfinity Store link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="support-list-id"]/li[3]/a').get_attribute('href'))

def test_MyAccounttFooterLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #My Account link
    element = driver.find_element(by=By.XPATH, value='//*[@id="my-account-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/myaccount/'

    if "https://business.comcast.com/myaccount/" in element: 
        print('My Account link available in global footer') 
    else: 
        print('My Account link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="my-account-header-id"]').get_attribute('href'))

    #Sign in link
    element = driver.find_element(by=By.XPATH, value='//*[@id="my-account-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/account/'

    if "https://business.comcast.com/account/" in element: 
        print('\n''Sign in link available in global footer') 
    else: 
        print('Sign in link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="my-account-list-id"]/li[1]/a').get_attribute('href'))

    #Cloud Solutions link
    element = driver.find_element(by=By.XPATH, value='//*[@id="my-account-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://cloudsolutions.comcast.com/en-US/home'

    if "https://cloudsolutions.comcast.com/en-US/home" in element: 
        print('\n''Cloud Solutions link available in global footer') 
    else: 
        print('Cloud Solutions link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="my-account-list-id"]/li[2]/a').get_attribute('href'))
    
def test_AboutUsFooterLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #About us link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/about-us'

    if "https://business.comcast.com/about-us" in element: 
        print('About us link available in global footer') 
    else: 
        print('About us link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-header-id"]').get_attribute('href'))

    #Why Comcast link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/about-us/comcast-business'

    if "https://business.comcast.com/about-us/comcast-business" in element: 
        print('\n''Why Comcast link available in global footer') 
    else: 
        print('Why Comcast link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[1]/a').get_attribute('href'))

    #Our network link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/about-us/our-network'

    if "https://business.comcast.com/about-us/our-network" in element: 
        print('\n''Our network link available in global footer') 
    else: 
        print('Our network link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[2]/a').get_attribute('href'))
    
    #Press Releases link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/about-us/press-releases'

    if "https://business.comcast.com/about-us/press-releases" in element: 
        print('\n''Press Releases link available in global footer') 
    else: 
        print('Press Releases link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[3]/a').get_attribute('href'))

    #Advertising link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://effectv.com/?utm_source=comcast_business&utm_medium=referral&utm_campaign=footer&utm_content=728x90'

    if "https://effectv.com/?utm_source=comcast_business&utm_medium=referral&utm_campaign=footer&utm_content=728x90" in element: 
        print('\n''Advertising link available in global footer') 
    else: 
        print('Advertising link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[4]/a').get_attribute('href'))

    #Comcast Business Promise link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/about-us/promise'

    if "https://business.comcast.com/about-us/promise" in element: 
        print('\n''Business Promise link available in global footer') 
    else: 
        print('Business Promise link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[5]/a').get_attribute('href'))
    
    #Careers link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://jobs.comcast.com/business'

    if "https://jobs.comcast.com/business" in element: 
        print('\n''Careers link available in global footer') 
    else: 
        print('Careers link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[6]/a').get_attribute('href'))
    
    #Awards link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[7]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/enterprise/awards'

    if "https://business.comcast.com/enterprise/awards" in element: 
        print('\n''Awards link available in global footer') 
    else: 
        print('Awards link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[7]/a').get_attribute('href'))
    
    #DEI link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[8]/a').get_attribute('href')
    assert element == 'https://corporate.comcast.com/values/diversity-equity-inclusion'

    if "https://corporate.comcast.com/values/diversity-equity-inclusion" in element: 
        print('\n''DEI link available in global footer') 
    else: 
        print('DEI link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[8]/a').get_attribute('href'))
    
    #Comcast Rise link
    element = driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[9]/a').get_attribute('href')
    assert element == 'https://www.comcastrise.com/'

    if "https://www.comcastrise.com/" in element: 
        print('\n''Comcast Rise link available in global footer') 
    else: 
        print('Comcast Rise link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="about-us-list-id"]/li[9]/a').get_attribute('href'))

def test_PartnersFooterLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #Partner link
    element = driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-header-id"]').get_attribute('href')
    assert element == 'https://business.comcast.com/partner'

    if "https://business.comcast.com/partner" in element: 
        print('Partner link available in global footer') 
    else: 
        print('Partner link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-header-id"]').get_attribute('href'))
    
    #Customer Referrals link
    element = driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://www.comcastbizleads.com/CustomerReferral/CreateCustomerReferral'

    if "https://www.comcastbizleads.com/CustomerReferral/CreateCustomerReferral" in element: 
        print('Customer Referrals link available in global footer') 
    else: 
        print('Customer Referrals  link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[1]/a').get_attribute('href'))
    

    #Authorized connectors link
    element = driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/partner/authorized-connector-program'

    if "https://business.comcast.com/partner/authorized-connector-program" in element: 
        print('\n''Authorized connectors link available in global footer') 
    else: 
        print('Authorized connectors link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[2]/a').get_attribute('href'))
    
    #Solution Advisors link
    element = driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/partner/solutions-provider-program'

    if "https://business.comcast.com/partner/solutions-provider-program" in element: 
        print('\n''Solution Advisors link available in global footer') 
    else: 
        print('Solution Advisors link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[3]/a').get_attribute('href'))

    #Alliance link
    element = driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://www.comcastbizleads.com/Register/CompanyTypeSelection/2'

    if "https://www.comcastbizleads.com/Register/CompanyTypeSelection/2" in element: 
        print('\n''Alliance link available in global footer') 
    else: 
        print('Alliance link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="partners-and-referrals-list-id"]/li[4]/a').get_attribute('href'))


def test_BottomFooterLinks(driver):

    driver.get('https://business.comcast.com/?disablescripts=true')
    driver.maximize_window()

    #Contact us link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[1]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/contact'

    if "https://business.comcast.com/contact" in element: 
        print('Contact us link available in global footer') 
    else: 
        print('Contact us link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[1]/a').get_attribute('href'))

    #Community link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[2]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/community/'

    if "https://business.comcast.com/community/" in element: 
        print('\n''Community link available in global footer') 
    else: 
        print('Community link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[2]/a').get_attribute('href'))

    #Privacy Policy link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[3]/a').get_attribute('href')
    assert element == 'https://www.xfinity.com/privacy/policy'

    if "https://www.xfinity.com/privacy/policy" in element: 
        print('\n''Privacy Policy link available in global footer') 
    else: 
        print('Privacy Policy link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[3]/a').get_attribute('href'))
    
    #Your Privacy Choices link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[4]/a').get_attribute('href')
    assert element == 'https://www.xfinity.com/privacy/manage-preference'

    if "https://www.xfinity.com/privacy/manage-preference" in element: 
        print('\n''Your Privacy Choices link available in global footer') 
    else: 
        print('Your Privacy Choices link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[4]/a').get_attribute('href'))
    
    #Notice at Collection link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[5]/a').get_attribute('href')
    assert element == 'https://www.xfinity.com/privacy/policy/staterights#california'

    if "https://www.xfinity.com/privacy/policy/staterights#california" in element: 
        print('\n''Notice at Collection link available in global footer') 
    else: 
        print('Notice at Collection link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[5]/a').get_attribute('href'))
    
    #Visitor Agreement link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[6]/a').get_attribute('href')
    assert element == 'https://www.xfinity.com/corporate/legal/visitorAgreement'

    if "https://www.xfinity.com/corporate/legal/visitorAgreement" in element: 
        print('\n''Visitor Agreement link available in global footer') 
    else: 
        print('Visitor Agreement link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[6]/a').get_attribute('href'))

    #Terms and Conditions link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[7]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/terms-conditions-smb'

    if "https://business.comcast.com/terms-conditions-smb" in element: 
        print('\n''Terms and Conditions link available in global footer') 
    else: 
        print('Terms and Conditions link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[7]/a').get_attribute('href'))
    
    #Sitemap link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[8]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/site-map'

    if "https://business.comcast.com/site-map" in element: 
        print('\n''Sitemap link available in global footer') 
    else: 
        print('Sitemap link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[8]/a').get_attribute('href'))
    
    #Open Source link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[9]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/opensource'

    if "https://business.comcast.com/opensource" in element: 
        print('\n''Open Source link available in global footer') 
    else: 
        print('Open Source link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[9]/a').get_attribute('href'))
    
    #Broadband Labels link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[10]/a').get_attribute('href')
    assert element == 'https://business.comcast.com/broadband-labels'

    if "https://business.comcast.com/broadband-labels" in element: 
        print('\n''Broadband labels link available in global footer') 
    else: 
        print('Broadband labels link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-nav-flow-footer-list-id"]/li[10]/a').get_attribute('href'))
    
    #Facebook link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-flow-footer"]/div[2]/div/a[1]').get_attribute('href')
    assert element == 'https://www.facebook.com/ComcastBusiness'

    if "https://www.facebook.com/ComcastBusiness" in element: 
        print('\n''Facebook link available in global footer') 
    else: 
        print('Facebook link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-flow-footer"]/div[2]/div/a[1]').get_attribute('href'))
    
    #LinkedIn link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-flow-footer"]/div[2]/div/a[2]').get_attribute('href')
    assert element == 'https://www.linkedin.com/company/comcast-business'

    if "https://www.linkedin.com/company/comcast-business" in element: 
        print('\n''LinkedIn link available in global footer') 
    else: 
        print('LinkedIn link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-flow-footer"]/div[2]/div/a[2]').get_attribute('href'))
    
    #Twitter link
    element = driver.find_element(by=By.XPATH, value='//*[@id="bsd-flow-footer"]/div[2]/div/a[3]').get_attribute('href')
    assert element == 'https://twitter.com/comcastbusiness'

    if "https://twitter.com/comcastbusiness" in element: 
        print('\n''Twitter link available in global footer') 
    else: 
        print('Twitter link NOT available in global footer')
    print("CTA URL: "+driver.find_element(by=By.XPATH, value='//*[@id="bsd-flow-footer"]/div[2]/div/a[3]').get_attribute('href'))
