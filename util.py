import requests
import time
import datetime

def get_klines(symbol, interval='1h', limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()

    result = []
    for candle in data:
        result.append({
            'time': datetime.datetime.fromtimestamp(candle[0] / 1000),
            'open': float(candle[1]),
            'high': float(candle[2]),
            'low': float(candle[3]),
            'close': float(candle[4]),
            'volume': float(candle[5]),
        })
    return result
