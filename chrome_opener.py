import pyautogui
import time
import os
from test import *

chrome_command = "google-chrome --incognito" 

def open_binomo(email,password):
    os.system(chrome_command)
    time.sleep(1) 
    url = "https://binomoidr.com/trading" 
    pyautogui.hotkey("ctrl", "l")  
    pyautogui.typewrite(url) 
    pyautogui.press("enter")  

    time.sleep(20)
    try:
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
    except Exception as e:
        print(f"Error: {e}")
    