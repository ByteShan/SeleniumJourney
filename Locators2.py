from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")
# CSS Locators
# Tag and ID
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("Username")
# Only ID
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("Username")
# Tag and Class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("Username")
# Class
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("Username")
# Tag and attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("Username")
# Tag, Class and attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("Username")
time.sleep(5)

print("Test Success")
driver.close()