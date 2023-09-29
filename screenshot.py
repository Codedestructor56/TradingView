from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


url = "https://km.iqoption.com/traderoom"  

options=webdriver.ChromeOptions()
options.binary_location = "/usr/local/bin/google-chrome"

# Create a Chrome WebDriver instance with options
driver = webdriver.Chrome(options=options)

try:
    print("We're here")
    driver.get(url)
    driver.implicitly_wait(20)  

    screenshot_file = "screenshot.png"  
    driver.save_screenshot(screenshot_file)

    print(f"Screenshot saved as {screenshot_file}")

finally:
    driver.quit()
