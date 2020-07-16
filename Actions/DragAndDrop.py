from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragAndDrop():

    def test1(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            # To directly drag and drop method
            actions.drag_and_drop(fromElement, toElement).perform()

            # Another Choice is to Click and hold source element and move that element to destination element
            # actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag And Drop Element Successful")
            time.sleep(2)
        except:
            print("Drag And Drop failed on element")

ff = DragAndDrop()
ff.test1()