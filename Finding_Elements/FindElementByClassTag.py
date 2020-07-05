from selenium import webdriver

class Findbyclasstag():
    def test(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)
        ElementByclass = driver.find_element_by_class_name("inputs")
        if ElementByclass is not None:
            print("Found an element class")

        #ElementBytag = driver.find_element_by_tag_name("a")
        ElementBytag = driver.find_element_by_tag_name("h1")
        text = ElementBytag.text
        if ElementBytag is not None:
            print("Found an Element tag name and text on element is :" +text)

obj1 = Findbyclasstag()
obj1.test()