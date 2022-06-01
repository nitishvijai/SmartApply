from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("../../chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
driver.close()