from selenium import webdriver

class FindbyXpathCss():
    def test(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(BaseUrl)
        ElementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        if ElementByXpath is not None:
            print("Found an element Xpath")

        ElementByCss = driver.find_element_by_css_selector("#displayed-text")
        if ElementByCss is not None:
            print("Found an Element Css ")

obj1 = FindbyXpathCss()
obj1.test()