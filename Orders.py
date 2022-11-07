import requests, os, json, pandas as pd

def order_list(endpoint, headers, status = "open", limit = 50):
    ord_list_url = endpoint + "/orders"
    params = {"status":status}
    r = requests.get(ord_list_url, headers=headers, params=params)
    data = r.json()
    return pd.DataFrame(data)

def order_cancel(endpoint, headers, order_id=""):
    if len(order_id)>1:
        ord_cncl_url = endpoint + "/orders/{}".format(order_id)
    else:
        ord_cncl_url = endpoint + "/orders"
    r = requests.delete(ord_cncl_url, headers=headers)
    return r.json()

# Example call: market_order("AMZN", 1, endpoint, headers)
def market_order(symbol, quantity, endpoint, headers, side="buy", tif="day"):
    ord_url = endpoint + "/orders"
    params = {"symbol": symbol,
              "qty": quantity,
              "side" : side,
              "type": "market",
              "time_in_force": tif}
    r = requests.post(ord_url, headers=headers, json=params)
    return r.json()

# Example call: market_order("AMZN", 1, 320, endpoint, headers)
def limit_order(symbol, quantity, limit_pr, endpoint, headers, side="buy", tif="day"):
    ord_url = endpoint + "/orders"
    params = {"symbol": symbol,
              "qty": quantity,
              "side" : side,
              "type": "limit",
              "limit_price" : limit_pr,
              "time_in_force": tif}
    r = requests.post(ord_url, headers=headers, json=params)
    return r.json()

# Example call: stop_order("AMZN", 1, 3185, endpoint, headers, "sell")   
def stop_order(symbol, quanitity, stop_price, endpoint, headers, side = "buy", tif = "day"):
    ord_url = endpoint + "/orders"
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
    ord_url = endpoint + "/orders"
    params = {"symbol" : symbol,
              "quantity" : quanitity,
              "side" : side,
              "type" : "stop_limit",
              "stop_price" : stop_price,
              "limit_price" : limit_price,
              "time_in_force" : tif}
    r = requests.post(ord_url, headers = headers, json = params)
    return r.json()

# Example call: stop_limit_order("AMZN", 1, 2, endpoint, headers, "sell") 
def trail_stop_order(symbol, quantity, trail_pr, endpoint, headers, side="buy", tif="day"):
    ord_url = endpoint + "/orders"
    params = {"symbol": symbol,
              "qty": quantity,
              "side" : side,
              "type": "trailing_stop",
              "trail_price" : trail_pr,
              "time_in_force": tif}
    r = requests.post(ord_url, headers=headers, json=params)
    return r.json()

# Example call: stop_limit_order("AMZN", 1, 2, endpoint, headers, "sell") 
def bracket_order(symbol, quantity, tplp, slsp, sllp, endpoint, headers, side="buy", tif="day"):
    ord_url = endpoint + "/orders"
    params = {
              "symbol": symbol,
              "qty": quantity,
              "side" : side,
              "type": "market",
              "time_in_force": tif,
              "order_class": "bracket",
              "take_profit" : {
                              "limit_price":tplp
                              },
              "stop_loss" : {
                            "stop_price": slsp,
                            "limit_price": sllp
                            }
              }
    r = requests.post(ord_url, headers=headers, json=params)
    return r.json()