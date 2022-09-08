import requests, os, json

def market_order(symbol, quanitity, endpoint, headers, side = "buy", tif = "day"):
    ord_url = endpoint + "/v2/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "market",
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()

# Example call: market_order("AMZN", 1, endpoint, headers)

def limit_order(symbol, quanitity, limit_pr, endpoint, headers, side = "buy", tif = "day"):
    ord_url = endpoint + "/v2/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "market",
              "limit_price" : limit_pr,
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()
    
# Example call: market_order("AMZN", 1, 320, endpoint, headers)