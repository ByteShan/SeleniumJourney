from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception], poll_frequency=2)

driver.get("https://www.cricbuzz.com/")
driver.find_element(By.LINK_TEXT, "Live Scores").click()

try:
    match = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "//*[@id='page-wrapper']/div[5]/div[2]/div/div[1]/div/div[2]/a/div/div[1]")))
    match.click()

except:
    print("There is an Error")

finally:
    print(driver.current_url)
    print(driver.title)
