from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElement():
    def test(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)

        ElementsByclass = driver.find_elements_by_class_name("inputs")

        if ElementsByclass is not None:
            print("Found these list of class elements {0} and length is {1}".format(ElementsByclass, str(len(ElementsByclass))))

        ElementsByTag = driver.find_elements_by_tag_name("a")
        length = len(ElementsByTag)

        if ElementsByTag is not None:
            print("Found an elements by tag . The length is " + str(length))


Obj1 = ListOfElement()
Obj1.test()