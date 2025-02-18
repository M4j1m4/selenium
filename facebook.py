from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import time 

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com")

input_id = "email"
input_pass = "pass"
login_id = "login"

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.ID, input_id))
)

username = driver.find_element(By.ID, input_id)


password = driver.find_element(By.ID, input_pass)


login = driver.find_element(By.NAME, login_id)
login.click()

time.sleep(50)




