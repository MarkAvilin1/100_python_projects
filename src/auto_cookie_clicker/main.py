from selenium import webdriver
import datetime

chrome_driver_path = "F:/PythonProjects/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

min_now = datetime.datetime.now().minute

while min_now == (min_now + 5):
    cookie.click()
    min_now = datetime.datetime.now().minute

money = driver.find_element_by_id("money")

print(money.text)
