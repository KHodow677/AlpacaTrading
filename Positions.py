import requests
import os
import json

# Example Call:
# positions(endpoint, headers)
def positions(endpoint, headers, symbol=""):
    if len(symbol)>1:
        pos_url = endpoint + "/positions/{}".format(symbol)
    else:
        pos_url = endpoint + "/positions"
    r = requests.get(pos_url, headers=headers)
    return r.json()

positions()