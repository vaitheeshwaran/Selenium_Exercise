from selenium import webdriver

class FirefoxTest():

    # basic function to get the google from Firefox driver
    def basicrun(self):
        # Provide the firefox driver path
        driver = webdriver.Firefox(executable_path="D:\study\python\FF_driver\geckodriver.exe")
        # Launch the google site
        driver.get("https://www.google.com")

Ff_obj1 = FirefoxTest()
Ff_obj1.basicrun()