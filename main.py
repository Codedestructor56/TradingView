import time
from tvDatafeed import TvDatafeedLive, Interval
import threading
import pinescript as p
from options_utils import *
from chrome_opener import *
def initialize_tv_datafeed():
    username = input("Enter your TradingView username (Press Enter to skip): ").strip()
    password = input("Enter your TradingView password (Press Enter to skip): ").strip()

    if username and password:
        tvl = TvDatafeedLive(username, password)
    else:
        tvl = TvDatafeedLive()
        print("You are using nologin method. Data access may be limited.")

    return tvl

def handle_data(seis, data):
    print(f"Received new data bar for {seis.symbol} - {seis.exchange} - {seis.interval.name}")
    print(data)

def curr_stats_print(current_state):
    print("Principal Amount: "+current_state[0]+"\n")
    print("Expiration Time: "+current_state[1]+"\n")
    print("Current Earnings percentage: "+str(current_state[2])+"\n")
    print("Current Account status: "+current_state[3]+"\n")
    print("Current Account Balance: "+current_state[4]+"\n")

def reload_webpage(last_reload_time):
    while True:
        if time.time() - last_reload_time >= 360:
            pyautogui.press('f5')
            last_reload_time = time.time() 
        time.sleep(60)

if __name__ == "__main__":
    tvl = initialize_tv_datafeed()
    symbol = input("Enter a valid symbol(must be supported by tradingview): ")
    symb=input('''Should a forward slash be added 'to the symbol's name?
                               For e.g: EURUSD will turn into EUR/USD for binomo symbol name compliance[y/N]: ''')
    exchanges = ["Pepperstone","OANDA","Forex.com","Eightcap","ICE","Capital.com","Saxo","Vantage"]
    print("Choose an exchange (enter the index):")
    for i, exchange in enumerate(exchanges):
        print(f"{i + 1}. {exchange}")
    try:
        user_choice = int(input("Enter the index of the exchange: "))
        if 1 <= user_choice <= len(exchanges):
            selected_exchange = exchanges[user_choice - 1]
            print(f"You selected: {selected_exchange}")
        else:
            raise Exception("Value not within range.")
    except ValueError:
        print("Invalid input. Please enter a valid index (numeric).")
    interval = Interval.in_1_minute
    email=input("Please enter your binomo email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise Exception("Not a valid email address.")
    password=input("Please enter your binomo password: ")
    open_binomo(email,password)
    print('''Please remove anything which covers the binomo dashboard from the screen
          within 10 seconds, minimization is an option.''')
    
    time.sleep(10)
    curr_state=get_curr_info(info_src)
    curr_stats_print(curr_state)
    if input("Do you want to switch your account?[y/N]: ").capitalize()=="Y":
        switch_accs(input("Which account mode should we switch to?[demo/real]: "))

    time.sleep(5)
    choose_option(symbol,symb.capitalize()=="Y")
    
    input("Press Enter to proceed")
    change_amount(int(input('''If you want to change your principal amount, type it here. If you don't,
                             just type 0: ''')))
    print('''Instructions for changing expiration time:
          1)Enter as many ticks as you'd like to achieve. Up until 5 ticks, it increases and decreases
          the time by a factor of 1 minute. After 5 ticks from the base expiration time, the interval is 
          15 minutes, so check your current expiration time status first and then choose the number of ticks.
          2)The time won't go beyond or below the assigned ranges on binomo's website, so choose the ticks wisely.''')
    ticks=int(input("Enter the number of ticks, enter 0 if you don't want to change the time: "))
    change_exp_time(ticks)
    
    print("Minimize your terminal and move it out of the way in 10 seconds")
    time.sleep(10)
    
    while True:
        last_reload_time = time.time()

        reload_thread = threading.Thread(target=reload_webpage, args=(last_reload_time,))
        reload_thread.daemon = True
        reload_thread.start()
        data = tvl.get_hist(symbol=symbol, exchange=selected_exchange, interval=interval, n_bars=10)
        result=p.apply_transformation(data)
        print(data)
        print(result['sma_value_volume'])
        print(result['trend_label'])
        print(result['arrows'])
        if get_curr_info(info_src)[2]>=70:
            change_exp_time(ticks)
            time.sleep(4)
            place_trade(int(result["arrows"][0]))
        # Wait for 2 minutes before the next iteration
        time.sleep(120)

