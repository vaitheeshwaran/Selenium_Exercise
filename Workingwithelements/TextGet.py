from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text

        # Another method to find the text, But we have to format string the output
        openTabElement1 = driver.find_element(By.ID, "opentab")
        elementText1 = openTabElement1.get_attribute("innerText")

        print("Text on element1 is: " + elementText)
        print("Text on element2 is: " + str(elementText1))
        time.sleep(1)
        driver.quit()


ff = GetText()
ff.test()