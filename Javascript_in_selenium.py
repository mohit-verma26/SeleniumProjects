import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore_certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")
time.sleep(5)