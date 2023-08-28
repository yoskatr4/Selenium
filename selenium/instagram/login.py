# Selenium'ı içeri aktar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# time modülünü t olarak içeri aktar
import time as t
# userInfo dosyasından email ve password'ü içeri aktar
from userInfo import email, password

# Instagram sınıfını tanımla
class Instagram:
    # İnitializer (yapıcı) fonksiyon, email ve password alır
    def __init__(self, email, password):
        # Firefox tarayıcısını başlat
        self.browser = webdriver.Firefox()
        # email ve password'ü sınıf özelliklerine kaydet
        self.email = email
        self.password = password

    # Giriş yapma fonksiyonunu tanımla
    def signIn(self):
        # Instagram giriş sayfasını aç
        self.browser.get("https://www.instagram.com/accounts/login/")
        # 3 saniye bekle (tarayıcının yüklenmesi için)
        t.sleep(3)
        
        # Kullanıcı adı giriş alanını bul ve email'i kullanarak tanımla
        email_input = self.browser.find_element(By.XPATH, "//input[@name='username']")
        # Parola giriş alanını bul ve password'u kullanarak tanımla
        password_input = self.browser.find_element(By.XPATH, "//input[@name='password']")

        # Email'i email giriş alanına gönder
        email_input.send_keys(self.email)
        # Password'u password giriş alanına gönder
        password_input.send_keys(self.password)
        # Enter tuşunu göndererek giriş yapmayı dene
        password_input.send_keys(Keys.ENTER)
        # 2 saniye bekle (girişin tamamlanması için)
        t.sleep(2)

# Instagram sınıfını oluştur ve email ile password'u kullanarak giriş yapmayı dene
instgrm = Instagram(email, password)
instgrm.signIn()
