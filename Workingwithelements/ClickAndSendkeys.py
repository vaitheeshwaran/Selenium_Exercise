from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"

        # Resolving for captcha issue [ take the profile path from putting (with // in windows ) in chrome browser: chrome://version/ ]
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\vaitheeshwaran.v\\AppData\Local\\Google\\Chrome\\User Data\\Default")
        driver = webdriver.Chrome(options=opt)

        driver.maximize_window()
        driver.get(baseUrl)

        # Every element check till 10 sec if it fails, if not fails it will do as it
        driver.implicitly_wait(20)

        # Click the sign in
        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        # Pass the email name
        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        # Pass the password
        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        # it will wait till 3 sec
        time.sleep(3)

        # Clear the entered email text
        emailField.clear()

        time.sleep(3)

        # again send the email
        emailField.send_keys("test1")
        driver.quit()



ff = ClickAndSendKeys()
ff.test()