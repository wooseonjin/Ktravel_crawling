from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(), options=options)
driver.get("https://www.naver.com")
time.sleep(5)
driver.quit()
