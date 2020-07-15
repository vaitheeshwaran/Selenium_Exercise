from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        # To avoid captcha issue
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\vaitheeshwaran.v\\AppData\Local\\Google\\Chrome\\User Data\\Default")
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)


        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        screenshotDirectory = "C:\\Users\\vaitheeshwaran.v\\Desktop\\"
        self.takeScreenshot(driver,screenshotDirectory)



    def takeScreenshot(self, driver,Directory):
        """
        Takes screenshot of the current open web page
        :param driver,Directory
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        destinationFile = Directory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()