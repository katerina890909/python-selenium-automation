import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
os.environ['PATH'] = os.pathsep + r"drivers"
driver = webdriver.Chrome()
driver.get("https://flyflat.ru/register/")
email = driver.find_element(By.NAME,'email')
email.send_keys('gth@mail.ru')
password = driver.find_element(By.NAME,'password')
password.send_keys('12tr5hgggggD.5')
username = driver.find_element(By.NAME,'username')
username.send_keys('Ekaterina')
city = driver.find_element(By.NAME,'city')
city.send_keys('Ulyanovck')
accept_policy = driver.find_element(By.NAME,'accept_policy')
submit = driver.find_element(By.CSS_SELECTOR,'[type="submit"]')
submit.click()
input("Для завершения программы нажмите Enter")
