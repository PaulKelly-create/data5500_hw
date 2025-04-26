#Get the data for api and test it
import alpaca_trade_api as tradeapi

ALPACA_API_KEY = 'YOUR_KEY'
ALPACA_SECRET_KEY = 'YOUR_SECRET'
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL)

def submit_order(ticker, side, qty=1):
    try:
        api.submit_order(
            symbol=ticker,
            qty=qty,
            side=side.lower(),
            type='market',
            time_in_force='day'
        )
        print(f"Alpaca paper order: {side.upper()} {qty} of {ticker}")
    except Exception as e:
        print(f"Order failed for {ticker}: {e}")

"""
# This version simulates Alpaca trading for testing purposes.

def submit_order(ticker, side, qty=1):

    print(f"[SIMULATED ORDER] {side.upper()} {qty} shares of {ticker}")
"""