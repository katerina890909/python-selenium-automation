import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
os.environ['PATH'] = os.pathsep + r"drivers"
driver = webdriver.Chrome
driver.get("https://demoqa.com/text-box")


input("Для завершения программы нажмите Enter")
