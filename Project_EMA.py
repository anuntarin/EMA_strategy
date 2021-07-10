import pandas as pd
import talib
import yfinance as yf
import datetime as dt


    #RSI
    price_['RSI'] = talib.RSI(price_['Adj Close'])
    price_['MACD1'], price_['MACD2'] , price_['MACD3'] = talib.MACD(price_['Adj Close'])
    price_['EMA25'] = talib.EMA(price_['Adj Close'], timeperiod=25)
    price_['EMA25_STD'] = price_['EMA25'] + price_.rolling(window=25)['EMA25'].std()
    
    price_['EMA50'] = talib.EMA(price_['Adj Close'], timeperiod=50)
    price_['EMA200'] = talib.EMA(price_['Adj Close'], timeperiod=200)
    
     #logic
    price_.loc[((price_.MACD1 >=0)
                &(price_.RSI>40)), 'logic1'] = 1
    price_.loc[((price_['Adj Close']< price_['EMA35_STD'])
                &(price_['Adj Close'] >price_.EMA35)), 'logic2'] = 1
    price_.loc[price_['Adj Close'] > price_.EMA50, 'logic3'] = 1
    price_.loc[price_['Adj Close'] > price_.EMA200, 'logic4'] = 1
    
    
    
    