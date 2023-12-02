from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h2[1]/a[1]").click()

print(driver.title)

driver.quit()