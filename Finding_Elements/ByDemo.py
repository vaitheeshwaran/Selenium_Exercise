from selenium import  webdriver
from selenium.webdriver.common.by import By

class ByDemo():
    def test(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)

        ElementById = driver.find_elements(By.ID, "name")

        if ElementById is not None:
            print("Found an element ID")
        ElementByXpath = driver.find_elements(By.XPATH, "//input[@id='displayed-text']")

        if ElementByXpath is not None:
            print("Found an element Xpath")

        ElementByLinkText = driver.find_elements(By.LINK_TEXT, "Login")

        if ElementByLinkText is not None:
            print("Found an element Link Text")

Obj1 = ByDemo()
Obj1.test()