from selenium import webdriver
import unittest
import time
class HMSLoginLogoutDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
        driver.get('http://www.seleniumbymahesh.com')
        driver.maximize_window()
    def test_login(self):
        driver.find_element_by_css_selector('#menu-item-186 > a:nth-child(1)').click()
        driver.find_element_by_name("username").send_keys("Admin")
        driver.find_element_by_name("password").send_keys("Admin")
        driver.find_element_by_name("submit").click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[2]/div/h3/a').click()
        time.sleep(10)
        driver.close()

unittest.main()