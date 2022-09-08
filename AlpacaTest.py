import requests
import os
import json
import pandas as pd
import HistoricalData

os.chdir("C:\\Users\\kyleh\\Documents\\Python\\Investing\\Alpaca")

headers = json.loads(open("key.txt","r").read())
endpoint = "https://data.alpaca.markets/v2"
symbols = ["FB","CSCO","AMZN"]



data_dump = HistoricalData.hist_data(symbols, headers, start="2022-01-01", timeframe="1Min")  

