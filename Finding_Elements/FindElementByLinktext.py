from selenium import webdriver

class Findbylinkpartial():
    def test(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)
        ElementByLink = driver.find_element_by_link_text("Login")
        if ElementByLink is not None:
            print("Found an element Link text")

        ElementByPartiallink = driver.find_element_by_partial_link_text("Practi")
        if ElementByPartiallink is not None:
            print("Found an Element Partial Link text ")

obj1 = Findbylinkpartial()
obj1.test()