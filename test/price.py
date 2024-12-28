import requests
from view import get_ticker


def get_price(name, mapping=False, url="https://api.upbit.com"):
    
    ticker = ','.join(get_ticker(name, mapping=mapping))
    params = {"markets": ticker}

    res = requests.get(url + "/v1/ticker", params=params)
    return res.json()
    
def get_all_prices(url="https://api.upbit.com"):
    params = {
        "quote_currencies": "KRW,BTC"
    }

    res = requests.get(url + "/v1/ticker/all", params=params)
    return res.json()
    
if __name__ == '__main__':
    name = '비트코인,이더리움'
    price = get_price(name, mapping=True)
    print(price)
    prices = get_all_prices()
    print(prices)