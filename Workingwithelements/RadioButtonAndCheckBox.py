from selenium import webdriver

import time

class RadioButtonAndCheckBox():
    def run(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)
        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)
        bmwCheckBox = driver.find_element_by_id("bmwcheck")
        bmwCheckBox.click()

        time.sleep(2)
        benzCheckBox = driver.find_element_by_id("benzcheck")
        benzCheckBox.click()

        # Print whether the radio button and checkbox has enabled
        print("BMW radio button is selected "+str(bmwRadioBtn.is_selected())) # Return True if selected , False if not selected
        print("Benz radio button is selected " + str(benzRadioBtn.is_selected()))
        print("BMW checkbox is selected " + str(bmwCheckBox.is_selected()))
        print("Benz checkbox is selected " + str(benzCheckBox.is_selected()))

RadioObj = RadioButtonAndCheckBox()
RadioObj.run()