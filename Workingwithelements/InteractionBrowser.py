from selenium import webdriver

class Bowser_Interaction_Method():

    def Interaction(self):
        BaseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        # Window Maximize
        driver.maximize_window()

        # Open the Url
        driver.get(BaseUrl)

        # Get Title
        title = driver.title
        Print("The current page Title is:", title)

        # Get the current Url
        CurrentUrl = driver.current_url
        print("Current url of the page is " + CurrentUrl)

        # Refresh the browser
        print("Browser refresh the first time")
        driver.get(CurrentUrl)
        print("Browser refresh the second time")

        # Open another url
        driver.get("https://letskodeit.teachable.com/sign_in")
        CurrentUrl = driver.current_url
        print("Current url of the page is " + CurrentUrl)

        # Browser Back ( Previous browser )
        print(" Goto the previous browser")
        driver.back()
        CurrentUrl = driver.current_url
        print("Current url of the page is " + CurrentUrl)

        # Browser Forward ( Next browser )
        print("Goto the next step browser")
        driver.forward()
        CurrentUrl = driver.current_url
        print("Current url of the page is " + CurrentUrl)

        # Get page source
        PageSoure = driver.page_source
        print("Page source is \n" + PageSoure)

        # Browser Quit / Close
        print("driver has closed")
        # driver.close()
        print("Driver has quitted")
        driver.quit()

Obj1 = Bowser_Interaction_Method()
Obj1.Interaction()