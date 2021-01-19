from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"F:\PythonProjects\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element_by_css_selector("#articlecount a")

# article_count.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Montenegro")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("Mark")

l_name = driver.find_element_by_name("lName")
l_name.send_keys("Avilin")

email = driver.find_element_by_name("email")
email.send_keys("avilin1@yahoo.com")

button = driver.find_element_by_tag_name("button")
button.send_keys(Keys.ENTER)
