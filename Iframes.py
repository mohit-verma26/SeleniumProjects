import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/tinymce")

driver.implicitly_wait(4)

driver.switch_to.frame("mce_0_ifr")

try:
    driver.find_element(By.ID, "tinymce").clear()

except Exception as e:
    print("currently the frame is in read only mode")


time.sleep(5)