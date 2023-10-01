import pyautogui
import time
import os
from test import *

chrome_command = "google-chrome --incognito" 
email=''
password=""
os.system(chrome_command)
time.sleep(3) 
url = "https://binomoidr.com/trading" 
pyautogui.hotkey("ctrl", "l")  
pyautogui.typewrite(url) 
pyautogui.press("enter")  

time.sleep(10)

if binomo_username:
    pyautogui.click(binomo_username)
    pyautogui.typewrite(email)
time.sleep(2)
if binomo_password:
    pyautogui.click(binomo_password)
    pyautogui.typewrite(password)
time.sleep(3)
if binomo_login:
    pyautogui.click(binomo_login)
else:
    print("Username field, password field, or Log In button not found.")