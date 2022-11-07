import alpaca_trade_api as tradeapi

def print_portfolio(headers, endpoint_default):
    api = tradeapi.REST(key_id=headers['APCA-API-KEY-ID'], secret_key=headers['APCA-API-SECRET-KEY'], base_url=endpoint_default)
    # Get a list of all of our positions.
    portfolio = api.list_positions()
    # Print the quantity of shares for each position.
    for position in portfolio:
        print("{} shares of {}".format(position.qty, position.symbol))