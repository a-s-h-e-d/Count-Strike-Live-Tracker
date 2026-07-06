import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(driver_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://cs2tracker.gg/stats/76561199103680570")
time.sleep(15)
cheat = driver.find_element(By.CSS_SELECTOR, ".mt-2.metric-label")
print(cheat.text)


driver.quit()