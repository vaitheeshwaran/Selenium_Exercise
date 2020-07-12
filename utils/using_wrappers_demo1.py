from selenium import webdriver
from utils.handy_wrappers import HandyWrappers
import time


class UsingWrappers1():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        # Pass the Locator as "name" and ID as default from destionaton method
        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)

        # Pass the Xpath locator and it's type to the object
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()
        time.sleep(3)

ff = UsingWrappers1()
ff.test()