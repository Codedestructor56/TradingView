import time
from tvDatafeed import TvDatafeedLive, Interval
import pinescript as p

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

if __name__ == "__main__":
    tvl = initialize_tv_datafeed()
    symbol = 'EURUSD'
    exchange = 'OANDA'
    interval = Interval.in_1_minute

    while True:
        data = tvl.get_hist(symbol=symbol, exchange=exchange, interval=interval, n_bars=10)
        result=p.apply_transformation(data)
        print(data)
        print(result['sma_value_volume'])
        print(result['trend_label'])
        print(result['arrows'])
        # Wait for 6 minutes before the next iteration
        time.sleep(120)

