from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.handy_wrappers import HandyWrappers
import time


class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-data-dir=C:\\Users\\vaitheeshwaran.v\\AppData\Local\\Google\\Chrome\\User Data\\Default")
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login into the account "
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Click on all courses text
        MyCourse = driver.find_element_by_partial_link_text("All Courses")
        MyCourse.click()

        # Search for courses -> You don't need to search the course
        # You can select it without searching also
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("Selenium")

        # Select Course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("Selenium WebDriver With Java")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        time.sleep(5)


ff = DynamicXPathFormat()
ff.test()