#Asked chat to give me some numbers to test my code before using a live URL 
#Helped me write some code to get random numbers into the data folder to test them

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

tickers = ['AAPL', 'GOOG', 'ADBE', 'TSLA', 'MSFT', 'NVDA', 'AMZN', 'META', 'NFLX', 'INTC']
start_date = datetime(2022, 1, 1)
end_date = datetime(2025, 1, 1)

def generate_prices(start_price=100, days=500):
    prices = [start_price]
    for _ in range(days - 1):
        change = np.random.normal(0, 1.5)  # Simulated daily change
        prices.append(max(1, prices[-1] + change))
    return prices

os.makedirs("data", exist_ok=True)

for ticker in tickers:
    dates = pd.date_range(start=start_date, end=end_date, freq='B')  # Business days
    prices = generate_prices(start_price=np.random.uniform(80, 300), days=len(dates))
    
    df = pd.DataFrame({
        "Date": dates,
        "Open": prices,
        "High": [p * np.random.uniform(1.00, 1.05) for p in prices],
        "Low": [p * np.random.uniform(0.95, 1.00) for p in prices],
        "Close": prices,
        "Volume": np.random.randint(1e6, 5e6, size=len(prices))
    })

    df.set_index("Date", inplace=True)
    df.to_csv(f"data{ticker}.csv")
    print(f"✅ Fake data generated for {ticker}")
