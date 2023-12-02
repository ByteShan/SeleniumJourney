from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")
print(driver.current_url)
driver.back()  # Snap
print(driver.current_url)
driver.forward()  # Ama
print(driver.current_url)

driver.refresh()

driver.quit()