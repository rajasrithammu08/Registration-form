from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("http://localhost:6789")
time.sleep(2)
print("Home Page Title:",driver.title)
text=driver.find_element(By.TAG_NAME,"h2").text
print("Page contains:",text)
time.sleep(3)
driver.quit()