from selenium import webdriver

chrome_driver_path = r"F:\PythonProjects\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

times = driver.find_elements_by_css_selector(".event-widget time")
events = driver.find_elements_by_css_selector(".event-widget li a")

output_events = {}
for i in range(len(times)):
    output_events[i] = {"time": times[i].text, "name": events[i].text, }

print(output_events)

driver.quit()
