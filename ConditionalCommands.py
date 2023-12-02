from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument('--headless=new')
driver = webdriver.Chrome(options=ops)
driver.maximize_window()

# driver.get("https://demo.nopcommerce.com/")
# search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print("Display Status: ", search_box.is_displayed())
# print("Enable Status: ", search_box.is_enabled())

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
male_button = driver.find_element(By.XPATH, "//input[@id='gender-male']")
female_button = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Default")

print(male_button.is_selected())
print(female_button.is_selected())

male_button.click()

print()
print("After Selecting Male")

print(male_button.is_selected())
print(female_button.is_selected())

female_button.click()
print()
print("After Selecting Female")
print(male_button.is_selected())
print(female_button.is_selected())

driver.quit()