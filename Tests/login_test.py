import time

from selenium import webdriver
import unittest
import sys
import os

from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.enter_username("Admin")
        lp.enter_password("admin123")
        lp.click_login()

        hp = HomePage(driver)
        hp.click_userdropdown()
        hp.click_logout()

        time.sleep(2)

    def test_02_login_invalid_username(self):
        driver = self.driver

        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.enter_username("Admin1")
        lp.enter_password("admin123")
        lp.click_login()
        message = driver.find_element(By.XPATH, "").text
        self.assertEqual(message, "Invalid credentials")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed Successfully")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Bhagyashree/workspace_python/ProjectObjectModelProject/reports'))


# To run on command prompt, run as administrator
# Navigate to:
# C:\Users\Bhagyashree\workspace_python\ProjectObjectModelProject
# Command:
# python -m Tests.login_test
