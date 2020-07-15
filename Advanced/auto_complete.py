from selenium import webdriver
from utils.handy_wrappers import HandyWrappers
import time

class AutoComplete():

    def run(self):
        baseUrl = "http://www.southwest.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        Handy_obj1 = HandyWrappers(driver)

        # Send Partial Data
        cityField = Handy_obj1.getElement("LandingAirBookingSearchForm_originationAirportCode")
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        Depart = "//button[@aria-label='New York Area Airports - New York (LaGuardia), NY - LGA']"
        itemToSelect = Handy_obj1.getElement(Depart, "xpath")
        itemToSelect.click()

        time.sleep(3)
        driver.quit()

ff = AutoComplete()
ff.run()