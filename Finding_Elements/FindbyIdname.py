from selenium import webdriver

class FindbyIdName():
    def test(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)
        ElementById = driver.find_element_by_id("name")
        if ElementById is not None:
            print("Found an element Id")

        ElementByName = driver.find_element_by_name("show-hide")
        if ElementByName is not None:
            print("Found an Element Name ")

obj1 = FindbyIdName()
obj1.test()