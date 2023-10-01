import pyautogui
import time
import os

chrome_command = "google-chrome --incognito" 
os.system(chrome_command)
time.sleep(3) 
url = "https://km.iqoption.com/traderoom" 
pyautogui.hotkey("ctrl", "l")  
pyautogui.typewrite(url) 
pyautogui.press("enter")  