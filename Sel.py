from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def open_browser(url, str):
    print('executing open_browser fun')
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (Windows-specific)
    options.add_argument("--no-sandbox")  # Bypass OS security model (Linux-specific)
    options.add_argument("--disable-dev-shm-usage")  # Overcome resource issues in containers

    browser = webdriver.Chrome(options=options)
    browser.get(url)
    print('url opened')
    text_box = browser.find_element(By.ID, "QR~QID9")
    print('textbox found')
    text_box.send_keys("Your data here")
    print('data entered')

    browser.quit()
    print('url closed')

open_browser('https://www.telltims.com/', 'abc')

