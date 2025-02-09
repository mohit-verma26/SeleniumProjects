import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(4)

driver.find_element(By.CLASS_NAME,"blinkingText").click()
windows_opened= driver.window_handles

driver.switch_to.window(windows_opened[1])

message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()

driver.switch_to.window(windows_opened[0])
driver.find_element(By.NAME,"username").send_keys(var)
driver.find_element(By.ID,"password").send_keys(var)
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"select[class='form-control']"))
dropdown.select_by_value("stud")

driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.alert.alert-danger.col-md-12')))

alert_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text
print(alert_message)


time.sleep(5)
