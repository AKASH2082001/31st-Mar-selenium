from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

username = input("enter the username: ")
password = input("enter the password: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
driver.find_element_by_name("username").send_keys(username)
time.sleep(2)
driver.find_element_by_name("password").send_keys(password)
time.sleep(2)
driver.find_element_by_class_name("qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(10)
driver.close()
print("Testccase Compeleted")

