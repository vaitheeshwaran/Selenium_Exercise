from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementList():

    def run(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # Take all radio button list with name as cars
        radioButtonList = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonList)
        print("Size of the radiobutton list"+str(size))


        for radioButton in radioButtonList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(4)

radioObj = ElementList()
radioObj.run()

