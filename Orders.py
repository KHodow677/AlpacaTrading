import requests, os, json

# Example call: market_order("AMZN", 1, endpoint, headers)
def market_order(symbol, quanitity, endpoint, headers, side = "buy", tif = "day"):
    ord_url = endpoint + "/v2/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "market",
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()

# Example call: market_order("AMZN", 1, 320, endpoint, headers)
def limit_order(symbol, quanitity, limit_price, endpoint, headers, side = "buy", tif = "day"):
    ord_url = endpoint + "/v2/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "limit",
              "limit_price" : limit_price,
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()

# Example call: stop_order("AMZN", 1, 3185, endpoint, headers, "sell")   
def stop_order(symbol, quanitity, stop_price, endpoint, headers, side = "buy", tif = "day"):
    ord_url = endpoint + "/v2/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "stop",
              "stop_price" : stop_price,
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()

# Example call: stop_limit_order("AMZN", 1, 3175, 3175, endpoint, headers, "sell")  
def stop_limit_order(symbol, quanitity, stop_price, limit_price, endpoint, headers, side = "buy", tif = "day"):
    ord_url = endpoint + "/v2/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "stop_limit",
              "stop_price" : stop_price,
              "limit_price" : limit_price,
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()