import requests


def get_all_tickers(mapping=False, url="https://api.upbit.com/v1/market/all?is_details=true"):
    headers = {"accept": "application/json"}
    resp = requests.get(url, headers=headers)
    
    if mapping:
        return {_resp['korean_name']: _resp['market'] for _resp in resp.json()}
    else:
        return resp.json()

def get_ticker(name, mapping=False, url="https://api.upbit.com/v1/market/all?is_details=true"):
    
    if isinstance(name, str):
        name = name.split(',')
    elif isinstance(name, list):
        pass 
    else:
        raise ValueError(f"NOT consider {name} for type{type(name)}")
    
    tickers = get_all_tickers(mapping=mapping, url=url)
    
    return [tickers[_name] for _name in name]

if __name__ == '__main__':
    tickers = get_all_tickers(mapping=True)
    print("tickers: ", tickers)
    ticker = get_ticker('비트코인,이더리움', mapping=True)
    print("ticker: ", ticker)
    
    