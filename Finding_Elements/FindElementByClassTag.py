from selenium import webdriver

class Findbyclasstag():
    def test(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)
        # If we provide complete class name such like "inputs distribute" , then it will not take, so we should take single name from the entire class by using css
        ElementByclass = driver.find_element_by_class_name("inputs")
        if ElementByclass is not None:
            print("Found an element class")
        # for below one it will take all the anchors tag element
        #ElementBytag = driver.find_element_by_tag_name("a")
        # below there is only one h1 tag, so there is no issue, mostly tag element will not be used
        ElementBytag = driver.find_element_by_tag_name("h1")
        text = ElementBytag.text
        if ElementBytag is not None:
            print("Found an Element tag name and text on element is :" +text)

obj1 = Findbyclasstag()
obj1.test()