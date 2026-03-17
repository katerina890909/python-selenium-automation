import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
d = webdriver.Chrome()
yield d
d.quit()
def test_login(driver):
driver.get("https://site.ru/login")
driver.find_element(By.ID, "user").send_keys("demo")
driver.find_element(By.ID, "pass").send_keys("secret")
driver.find_element(By.ID, "loginBtn").click()
WebDriverWait(driver, 5).until(
EC.visibility_of_element_located((By.CSS_SELECTOR,

".cabinet"))
)
assert "Кабинет" in driver.title