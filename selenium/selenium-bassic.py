from selenium import webdriver
import time

driver = webdriver.Firefox()  #driver seçiyoruz

url = "https://github.com/yoskatr4"

driver.get(url) # url i aç

time.sleep(2)
driver.maximize_window() # f11
driver.save_screenshot("Github-homepage.png") # ekarnın isimli bir klasöre kayd eder
print(driver.title)     #sayfanın title etiketini yazdır

url = "https://github.com"
driver.get(url)

print(driver.title)

if "Let’s build from here" in driver.title:     #eğer linkte titlede Let’s build from here varsa ss al
    driver.save_screenshot("githup.png")

time.sleep(2)

driver.back() #önceki sayfaya gir
# driver.forward() # sonraki sayfaya git

time.sleep(2)
driver.close() #tarayıcıyı kapar