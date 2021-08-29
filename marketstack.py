import os
import requests
import json


marketstack_key = os.environ.get('marketstack_key')
api_url = 'https://api.marketstack.com/vi/'

def  get_stock_price(stock_symbol):
    params = {
        'access_key': marketstack_key
    }
    end_point = ''.join([api_url,'tickers/',stock_symbol])
    api_result = requests.get(end_point,params)
    json_result = json.loads(api_result.text)
    return  {
        'last_price':json_result['last']
        
    }