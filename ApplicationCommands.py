from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)
Source = driver.page_source
with open("C:\\Users\\HP\\Downloads\\Sel.txt", "w") as file:
    file.write(Source)
driver.quit()
