import pyautogui
import time
from test import *
import re
import pyperclip
def copy_text(source,destination):

    pyautogui.moveTo(source[0], source[1])
    time.sleep(1)

    pyautogui.mouseDown()
    pyautogui.move(destination[0]-source[0], destination[1]-source[1], duration=0.2) 
    pyautogui.mouseUp()

    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()

def choose_option(name):
    pyautogui.click(add_option)
    time.sleep(1)
    pyautogui.click(add_option_search)
    time.sleep(1)
    pyautogui.typewrite(name)
    time.sleep(1)
    pyautogui.click(first_option)
    time.sleep(1)
    pyautogui.click(add_option)

def get_curr_info(coord_dict):
    info_list=[]
    time.sleep(1)
    info_list.append(copy_text(coord_dict['amount'][0],coord_dict['amount'][1]))
    info_list.append(copy_text(coord_dict['time'][0],coord_dict['time'][1]))
    info_list.append(int(re.findall(r'\d+', copy_text(coord_dict['earnings'][0],coord_dict['earnings'][1]))[0]))
    text = copy_text(coord_dict['curr_bal'][0], coord_dict['curr_bal'][1])
    text = re.sub(r'\s', '', text)
    text = re.sub(r'\$', '', text)
    info_list.append(text)
    pyautogui.click(release)
    return info_list

def place_trade(signal):
    if signal==1:
        pyautogui.click(go_down)
    elif signal ==-1:
        pyautogui.click(go_up)

choose_option("EUR/USD")
print(get_curr_info({'amount':[amt_src,amt_dest],'time':[time_source,time_dest],'earnings':[earnings_source,earnings_dest]
                     ,'curr_bal':[curr_balance_source,curr_balance_dest]}))
place_trade(-1)


