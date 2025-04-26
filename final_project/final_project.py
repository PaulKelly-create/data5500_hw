import os
import json
import pandas as pd
from fetch_data import update_stock_data
from strategies import mean_reversion, sma_crossover, custom_strategy
from alpaca_trader import submit_order
#Got the tickers for 10 different stocks
tickers = ['AAPL', 'GOOG', 'ADBE', 'TSLA', 'MSFT', 'NVDA', 'AMZN', 'META', 'NFLX', 'INTC']
results = {}

best = {'stock': None, 'strategy': None, 'profit': float('-inf')}
#Run the data through the strategies to see what works
for ticker in tickers:
    df = update_stock_data(ticker)
    prices = df['Close'].dropna().tolist()

    strategies = {
        "MeanReversion": mean_reversion,
        "SMA_Crossover": sma_crossover,
        "Momentum": custom_strategy
    }

    for name, strategy_func in strategies.items():
        profit, ret, signal = strategy_func(prices)
        results[f"{ticker}_{name}"] = {
            "profit": profit,
            "return_pct": ret,
            "signal_today": signal
        }

        if profit > best['profit']:
            best.update(stock=ticker, strategy=name, profit=profit)

        if signal:
            print(f"{ticker} - {name}: You should {signal} this stock today.")
            submit_order(ticker, signal)
#Write the json file to save what would be best for selling
with open("results.json", "w") as f:
    json.dump({'results': results, 'best': best}, f, indent=4)

print(f"\n Best performer: {best['stock']} using {best['strategy']} with profit ${best['profit']}")
