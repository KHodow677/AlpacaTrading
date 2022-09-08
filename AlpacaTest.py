import requests, os, json
import pandas as pd

# Other Files
import HistoricalData, Orders
import alpaca_trade_api as tradeapi

# Set current directory
os.chdir("C:\\Users\\kyleh\\Documents\\Python\\Investing\\AlpacaTrading")

# Load headers from key text file key.txt to log in and set alpaca site endpoint
headers = json.loads(open("key.txt","r").read())
endpoint = "https://api.alpaca.markets/v2"
data_endpoint = "https://data.alpaca.markets/v2"

# Check if the market is open now.
clock_url = endpoint + "/clock"
r = requests.get(clock_url, headers = headers)
r = r.json()
print('The market is {}'.format('open.' if r["is_open"] else 'closed.'))

if (r["is_open"]):
    # List of Stocks
    symbols = ["AMZN"]

    # Gather historical data and store in dictionary of dataframes
    data_dump = HistoricalData.hist_data(symbols, data_endpoint, headers, start="2022-07-01", timeframe="1Min")  

