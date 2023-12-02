from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/")

sliders = driver.find_elements(By.TAG_NAME, "li")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

driver.quit()