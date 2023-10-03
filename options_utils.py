import pyautogui
import time
from test import *
import re
import pyperclip
import datetime

info_src={'amount':[amt_src,amt_dest],
          'time':[time_source,time_dest],
          'earnings':[earnings_source,earnings_dest],
          'curr_bal':[curr_balance_source,curr_balance_dest],
          'acc_type':[acc_type_src,acc_type_dest]}

def copy_text(source,destination):

    pyautogui.moveTo(source[0], source[1])
    time.sleep(1)

    pyautogui.mouseDown()
    pyautogui.move(destination[0]-source[0], destination[1]-source[1], duration=0.2) 
    pyautogui.mouseUp()

    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()

def choose_option(name,add_forwslash:bool):
    if add_forwslash:
        name = name[:3]+"/"+name[3:]
    pyautogui.click(add_option)
    time.sleep(1)
    pyautogui.click(add_option_search)
    time.sleep(0.1)
    pyautogui.typewrite(name)
    time.sleep(0.1)
    pyautogui.click(first_option)
    time.sleep(0.1)
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
    info_list.append(copy_text(coord_dict['acc_type'][0],coord_dict['acc_type'][1]))
    pyautogui.click(release)
    return info_list

def place_trade(signal):
    if signal==1:
        pyautogui.click(go_down)
    elif signal ==-1:
        pyautogui.click(go_up)

def change_amount(ch_amt):
    pyautogui.click(amt_dest[0], amt_dest[1])
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    pyautogui.typewrite(str(ch_amt))
    time.sleep(0.5)
    pyautogui.click(release)

def switch_accs(choice):
    try:
        pyautogui.click(curr_balance_dest)
        if choice=="demo":
            pyautogui.click(demo_acc)
        elif choice=="real":
            pyautogui.click(real_acc)
        else:
            raise ValueError("Enter a valid account type")
        time.sleep(0.25)
        pyautogui.click(trade_message)
    except:
        print(f"Error occured, try choosing between demo and real")

def convert_time_string_to_datetime(time_str):
    hours, minutes = map(int, time_str.split(':'))

    current_date = datetime.date.today()
    exp_time = datetime.datetime(current_date.year, current_date.month, current_date.day, hours, minutes)
    
    return exp_time
def change_exp_time(addition):
    curr_exp_time_str=get_curr_info(info_src)[1]
    curr_exp_time = convert_time_string_to_datetime(curr_exp_time_str)
    new_exp_time = curr_exp_time + datetime.timedelta(minutes=int(addition))
    current_time = datetime.datetime.now()
    if new_exp_time >= current_time:
        if addition > 0:
            for _ in range(abs(addition)):
                pyautogui.click(time_increase[0], time_increase[1])
        elif addition < 0:
            for _ in range(abs(addition)):
                pyautogui.click(time_decrease[0], time_decrease[1])
        else:
            return

    else:
        return curr_exp_time_str
