from selenium import webdriver
import time

class GetAttribute():
    def run(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(BaseUrl)

        element = driver.find_element_by_id("name")
        resultValue = element.get_attribute("placeholder")
        # Print the Value of the attribute

        print("The value of the placeholder: " +str(resultValue))
        time.sleep(3)
        driver.quit()

Valueobj1 = GetAttribute()
Valueobj1.run()