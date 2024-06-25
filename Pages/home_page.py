from selenium.webdriver.common.by import By
from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.user_dropdown_xpath = Locators.user_dropdown_xpath
        self.logout_link_xpath = Locators.logout_link_xpath

    def click_userdropdown(self):
        self.driver.find_element(By.XPATH, self.user_dropdown_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()
