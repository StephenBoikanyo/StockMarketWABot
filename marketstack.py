import os
import requests
import json


MARKETSTACK_KEY = os.environ.get('MARKETSTACK_KEY')
api_url = 'http://api.marketstack.com/v1/'

def  get_stock_price(stock_symbol):
    params = {
        'access_key': MARKETSTACK_KEY
    }
    end_point = ''.join([api_url,'tickers/',stock_symbol,'/intraday/latest'])
    api_result = requests.get(end_point,params)
    json_result = json.loads(api_result.text)
    return  {
        'last_price':json_result['last']
        
    }