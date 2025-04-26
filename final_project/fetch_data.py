#Getting the data, with the right dats to have and test
import yfinance as yf
import pandas as pd
import os

def update_stock_data(ticker, start="2020-01-01"):
    os.makedirs("data", exist_ok=True)
    filename = f"data/{ticker}.csv"
    try:
        df_existing = pd.read_csv(filename, index_col="Date", parse_dates=True)
        last_date = df_existing.index[-1]
        new_data = yf.download(ticker, start=last_date.strftime('%Y-%m-%d'))
        df_updated = pd.concat([df_existing, new_data[~new_data.index.isin(df_existing.index)]])
    except FileNotFoundError:
        df_updated = yf.download(ticker, start=start)

    df_updated.to_csv(filename)
    print(f"{ticker} updated. Last date: {df_updated.index[-1].date()}")
    return df_updated

"""
#To test the randomized data before using a live URL
import pandas as pd

def update_stock_data(ticker, start="2020-01-01"):
    filename = f"data{ticker}.csv"
    df = pd.read_csv(filename, index_col="Date", parse_dates=True)
    print(f"{ticker} loaded from local CSV. Last date: {df.index[-1].date()}")
    return df
"""