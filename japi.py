import sys
import pandas as pd
from alpha_vantage.timeseries import TimeSeries 

API_KEY = '1Z0F0BWGMSBGGWSR'


def getStockdata(symbol):
    try:
        ts = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = ts.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:
        return "Stock Symbol incorrect"


def main():
    f = open('japi.out', 'w')
    while 1:
        user_input = input("Type the stock symbol to get the price or quit to exit\n").upper()
        if user_input != "QUIT":
            response = 'The current price of {} is {}\n'.format(user_input, getStockdata(user_input))
            print(response)
            f.write(response)
        else:
            raise SystemExit


print "Stock Quotes retrieved successfully!"

main()
