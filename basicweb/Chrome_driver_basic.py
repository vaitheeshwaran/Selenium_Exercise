from selenium import webdriver

class ChromeTest():
    def basicrun(self):
        driver = webdriver.Chrome(executable_path="D:\study\python\Ch_driver\chromedriver.exe")
        driver.get("https://www.google.com")

ch_Obj1 = ChromeTest()
ch_Obj1.basicrun()