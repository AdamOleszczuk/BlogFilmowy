import time
from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get(url="http://127.0.0.1:8000/admin")


def element_is_clickable():

    driver.find_element("xpath", '//*[@id="id_username"]').send_keys('admin')
    driver.find_element("xpath", '//*[@id="id_password"]').send_keys('haslo123')
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="user-tools"]/a[1]').click()
    driver.find_element("xpath", '/html/body/nav/header/div[2]/a').click()

#element_is_clickable()

def respons_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)

# respons_check(900, "test900.png")
# respons_check(1200, "test1200.png")
# respons_check(1800, "test1800.png")
# respons_check(600, "test600.png")