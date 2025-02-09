import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("mohit")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("mohit")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown =  Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_visible_text("Male")
driver.find_element(By.XPATH, "//label[normalize-space()='Student']").click()
driver.find_element(By.NAME, "bday").send_keys("26-04-1999")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')))

alert_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
print(alert_message)

time.sleep(5)