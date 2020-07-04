from selenium import webdriver

class FirefoxTest():
    def basicrun(self):
        driver = webdriver.Firefox(executable_path="D:\study\python\FF_driver\geckodriver.exe")
        driver.get("https://www.google.com")

Ff_obj1 = FirefoxTest()
Ff_obj1.basicrun()