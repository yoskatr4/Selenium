from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t


driver = webdriver.Firefox()

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element_by_name("q")
t.sleep(1)
searchInput.send_kesy("python")
t.sleep(2)
searchInput.send_kesy(Keys.ENTER)
t.sleep(2)


driver.close()