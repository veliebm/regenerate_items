from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://benvelie.com/ben.html")
while True:
    time.sleep(0.5)
    element = driver.find_element(By.CLASS_NAME, "ben")
    element.click()
