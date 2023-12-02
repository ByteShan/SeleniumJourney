from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument('--headless=new')

driver = webdriver.Chrome(options=ops)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(elements))

with open("C:\\Users\\HP\\Downloads\\Sel.txt", "w") as file:
    for ele in elements:
        print(ele.text)