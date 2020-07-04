from selenium import webdriver

class ChromeTest():

# basic function to get the google from chrome driver
    def basicrun(self):
        # Provide the chrome driver path
        driver = webdriver.Chrome(executable_path="D:\study\python\Ch_driver\chromedriver.exe")
        # Launch the google site
        driver.get("https://www.google.com")

ch_Obj1 = ChromeTest()
ch_Obj1.basicrun()