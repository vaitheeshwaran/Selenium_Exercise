from selenium import webdriver

class FirefoxTest():

    # basic function to get the google from Firefox driver
    def basicrun(self):
        # Provide the firefox driver path
        # driver = webdriver.Firefox(executable_path="D:\study\python\Drivers\geckodriver.exe")
        # Without The Driver path set ( For Linux all drivers put together into /usr/local/bin directory, In Windows add the system path in enviroinment variables )
        driver = webdriver.Firefox()
        # Launch the google site
        driver.get("https://www.google.com")

Ff_obj1 = FirefoxTest()
Ff_obj1.basicrun()