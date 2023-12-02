from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://money.rediff.com/gainers")

# Self
# Txt_Msg = driver.find_element(By.XPATH, "//a[normalize-space()='Morgan Ventures Ltd.']/self::a").text

# Parent
# Txt_Msg = driver.find_element(By.XPATH, "//a[normalize-space()='Morgan Ventures Ltd.']/parent::td").text

# Child
children = driver.find_elements(By.XPATH, "//a[normalize-space()='Morgan Ventures Ltd.']/ancestor::tr/child::td")
print(len(children))

# Ancestor
Txt_Msg = driver.find_element(By.XPATH, "//a[normalize-space()='Morgan Ventures Ltd.']/ancestor::tr").text
print(Txt_Msg)

driver.quit()