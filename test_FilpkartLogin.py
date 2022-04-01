from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Filpkart")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_class_name("LC20lb.MBeuO.DKV0Md").click()
time.sleep(2)
# driver.find_element_by_class_name("_1_3w1N").click()
# time.sleep(2)
driver.find_element_by_class_name("_2IX_2-.VJZDxU").send_keys("9962873499")
time.sleep(2)
driver.find_element_by_class_name("_2IX_2-._3mctLh.VJZDxU").send_keys("@Pakash208")
time.sleep(2)
driver.find_element_by_class_name("_2KpZ6l._2HKlqd._3AWRsL").click()
time.sleep(10)
driver.find_element_by_name("q").send_keys("poco x3")
time.sleep(2)
driver.find_element_by_class_name("_34RNph").click()
time.sleep(2)
driver.find_element_by_partial_link_text("18,990").click()
time.sleep(5)
driver.close()
print("Testcase Completed")






