import os
import time
# os.environ['PATH'] = os.pathsep + r"drivers"
# driver = webdriver.Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_smoke():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options) 

    driver.get("https://demoqa.com/text-box")
    full_name = driver.find_element(By.ID,value='userName')
    full_name.send_keys('Katya')
    email = driver.find_element(By.ID, value='userEmail')
    email.send_keys('gth@mail.ru')
    current_Address = driver.find_element(By.ID, value='currentAddress')
    current_Address.send_keys('Address 1')
    permanent_Address = driver.find_element(By.ID, value='permanentAddress')
    permanent_Address.send_keys('Address 2')
    submit = driver.find_element(By.ID, value='submit')
    assert submit.text == "Submit", "Unoxpected text on button"
    """ submit.click() """
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(10)



    # driver.quit()
    # assert True, ""




