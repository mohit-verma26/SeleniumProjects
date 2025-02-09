import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser_sorted_list = []

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.implicitly_wait(4)
driver.find_element(By.XPATH, "//span[normalize-space()='Veg/fruit name']").click()
veggies = driver.find_elements(By.XPATH, "//tr//td[1]")

for veggie in veggies:
    browser_sorted_list.append(veggie.text)

our_sorted_veggies = browser_sorted_list.copy()

browser_sorted_list.sort()

assert browser_sorted_list==our_sorted_veggies

print("Successfully Sorted")


time.sleep(5)