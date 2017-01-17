from behave import *
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement



@Given('I have a valid login account')
def precondition(self, username="admin", password="admin", site_url="http://lms-stag-th.lzd.co/"):
    self.username = username
    self.password = password
    self.site_url = site_url


@step('I enter login account and try to login')
def login(self, driver=webdriver.Chrome()):
    txtUsername = "//*[@id='username']"
    txtPassword = "//*[@id='password']"
    btnLogin = "//*[@id='_submit']"
    self.driver = driver
    driver.get(self.site_url)
    driver.find_element_by_xpath(txtUsername).send_keys(self.username)
    driver.find_element_by_xpath(txtPassword).send_keys(self.password)
    driver.find_element_by_xpath(btnLogin).click()

@then('I am able to login successfully')
def verify(self):
    linkLogout = "//*[@id='navbar-example']/div/div[2]/ul[2]/li[2]/a"
    # self.driver.find_element_by_xpath(linkLogout).click()
    logout = self.driver.find_element_by_xpath(linkLogout)
    if logout.get_attribute('text') == 'Logpout':
        logout.find_element_by_xpath(linkLogout).click()
        self.driver.close()
        return True
    else:
        # self.driver.close()
        return False

