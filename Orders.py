import requests, os, json

def market_order(symbol, quanitity, side, tif, endpoint, headers):
    ord_url = endpoint + "/v2/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "market",
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()
    
