import requests
from view import get_ticker

UNITS = ['seconds', 'minutes', 'days', 'weeks', 'months', 'years']
MIN_UNITS = [1, 3, 5, 15, 10, 30, 60, 240]
MAX_COUNT = 200

def get_candle(name, count, to, unit, min_unit=1,
               mapping=False,
               url="https://api.upbit.com/v1/candles/"):
    
    assert unit in UNITS, ValueError(f"Unit must be one of {UNITS}")
    assert min_unit in MIN_UNITS, ValueError(f"Min-unit must be one of {MIN_UNITS}")
    assert count <= MAX_COUNT, ValueError(f"Count must be lower than {MAX_COUNT}")
    
    url += unit
    if unit == 'minutes':
        url += f'/{str(min_unit)}'
    
    ticker = get_ticker(name, mapping=mapping)
    params = {  
        'market': ticker,  
        'count': count,
        'to': to
    }  
    resp = get_candle_by_params(params, url=url)    

    return resp.text

def get_candle_by_params(params, url):
    headers = {"accept": "application/json"}
    resp = requests.get(url, params=params, headers=headers)

    return resp
    
    
if __name__ == '__main__':
    name = '비트코인'
    count = 1
    to = '2024-10-01 00:00:00'
    # unit = 'seconds'
    unit = 'minutes'
    min_unit = 10
    
    candle = get_candle(name, count, to, unit, min_unit=min_unit, mapping=True)
    print(candle)