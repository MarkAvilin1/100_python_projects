from selenium import webdriver
import datetime

chrome_driver_path = "C:/PythonProjects/100_python_projects/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

current_time = datetime.datetime.now().minute
finish_time = int(current_time + 5)

while current_time < finish_time:
    cookie.click()
    current_time = datetime.datetime.now().minute

money = driver.find_element_by_id("money")

print(money.text)
