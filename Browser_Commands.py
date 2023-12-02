import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)

print(driver.title)

driver.close()