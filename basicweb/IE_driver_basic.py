from selenium import webdriver
class IE_basic():

    # basic function to get the google from IE driver
    def basicrun(self):
        # Provide the IE driver path
        # driver = webdriver.Ie(executable_path="D:\study\python\Drivers\IEDriverServer.exe")
        # Without The Driver path set ( For Linux all drivers put together into /usr/local/bin directory, In Windows add the system path in enviroinment variables )
        driver = webdriver.Ie()
        # Launch the google site
        driver.get("http://www.google.com")

IE_Obj1 = IE_basic()
IE_Obj1.basicrun()