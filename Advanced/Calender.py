from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.handy_wrappers import HandyWrappers
import time

class Calender_Selection():

    def selection_date(self):
        BaseUrl = "https://www.expedia.co.in/"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)
        driver.maximize_window()
        driver.implicitly_wait(8)

        Flights_tab = "//span[contains(text(),'Flights')]"
        # We can use position when find the xpath, but below xpath did not worked
        # Flights_tab = "//section[@class='cal-month']//[position()=1]//a[text(),'31']"
        dep = "//button[@id='d1-btn']"
        dep_dt = "//table[@class='uitk-new-date-picker-weeks']//button[starts-with(@aria-label, '14 Jul')]"
        ret_dt = "//table[@class='uitk-new-date-picker-weeks']//button[starts-with(@aria-label, '15 Jul')]"
        done = "//button[@data-stid='apply-date-picker']/span"

        handy_obj1 = HandyWrappers(driver)
        # Go to the flight page
        Flight1 = handy_obj1.getElement(Flights_tab,"xpath")
        Flight1.click()
        # Going to the Date page
        dep_ele = handy_obj1.getElement(dep,"xpath")
        dep_ele.click()
        # click the departure date
        dep_dt_ele = handy_obj1.getElement(dep_dt, "xpath")
        dep_dt_ele.click()
        # Click the return date
        ret_dt_ele = handy_obj1.getElement(ret_dt, "xpath")
        ret_dt_ele.click()
        # Click the Done button
        done_click = handy_obj1.getElement(done, "xpath")
        done_click.click()

        driver.quit()


Calender_obj1 = Calender_Selection()
Calender_obj1.selection_date()