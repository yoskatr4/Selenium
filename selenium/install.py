from selenium import webdriver

driver = webdriver.Firefox()  #driver seçiyoruz

url = "https://github.com/yoskatr4"

driver.get(url) # url i aç