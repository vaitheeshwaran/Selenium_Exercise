from selenium import webdriver
from utils.handy_wrappers import HandyWrappers
import time

class Calender_Selection():

    def run(self):
        BaseUrl = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.get(BaseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        Flights_tab = "//span[contains(text(),'Flights')]"
        # We can use position when find the xpath, but below xpath did not worked
        # Flights_tab = "//section[@class='cal-month']//[position()=1]//a[text(),'31']"
        dep_dt_id = "flight-departing-hp-flight"
        handy_obj1 = HandyWrappers(driver)
        Flight1 = handy_obj1.getElement(Flights_tab,"xpath")
        Flight1.click()
        dep_dt = handy_obj1.getElement(dep_dt_id)
        dep_dt.send_keys("07/14/2020")
        time.sleep(3)
        driver.quit()

Calender_obj1 = Calender_Selection()
Calender_obj1.run()