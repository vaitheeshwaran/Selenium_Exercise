from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.handy_wrappers import HandyWrappers
import time


class ElementPresentCheck():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        # Return true by passing right ID
        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        # Return False by passing wrong xpath
        elementResult2 = hw.elementPresenceCheck("//input[@id='name1']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()