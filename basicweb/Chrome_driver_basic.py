from selenium import webdriver
import os

class ChromeTest():

# basic function to get the google from chrome driver
    def basicrun(self):
        # Provide the chrome driver path
        # driver = webdriver.Chrome(executable_path="D:\study\python\Drivers\chromedriver.exe")
        # if this programs runs to different OS platform, then Above will not worked. check below
        #driverlocation = "D:\study\python\Drivers\chromedriver.exe"
        #os.environ("Webdriver chrome location") = driverlocation
        driver = webdriver.Chrome(driverlocation)
        # Without The Driver path set ( For Linux all drivers put together into /usr/local/bin directory, In Windows add the system path in enviroinment variables )
        driver = webdriver.Chrome()
        # Launch the google site
        driver.get("https://www.google.com")

ch_Obj1 = ChromeTest()
ch_Obj1.basicrun()