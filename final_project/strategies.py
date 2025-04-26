#Looked at past assingment for the different strategies and used them again
def mean_reversion(prices):
    profit = 0
    position = None
    sell_queue = []
    signal_today = None

    for i in range(5, len(prices)):
        avg = sum(prices[i-5:i]) / 5
        price = prices[i]

        if price < avg * 0.98:
            if sell_queue:
                sell_price = sell_queue.pop(0)
                profit += sell_price - price
            elif position is None:
                position = price
        elif price > avg * 1.02:
            if position is not None:
                profit += price - position
                position = None
            else:
                sell_queue.append(price)

    avg = sum(prices[-5:]) / 5
    if prices[-1] < avg * 0.98:
        signal_today = "BUY"
    elif prices[-1] > avg * 1.02:
        signal_today = "SELL"

    return round(profit, 2), round((profit / prices[0]) * 100, 2), signal_today


def sma_crossover(prices, short_window=5, long_window=20):
    profit = 0
    position = None
    sell_queue = []
    signal_today = None

    for i in range(long_window, len(prices)):
        short_avg = sum(prices[i-short_window:i]) / short_window
        long_avg = sum(prices[i-long_window:i]) / long_window
        price = prices[i]

        if short_avg > long_avg:
            if sell_queue:
                sell_price = sell_queue.pop(0)
                profit += sell_price - price
            elif position is None:
                position = price
        elif short_avg < long_avg:
            if position is not None:
                profit += price - position
                position = None
            else:
                sell_queue.append(price)

    short_avg = sum(prices[-short_window:]) / short_window
    long_avg = sum(prices[-long_window:]) / long_window
    if short_avg > long_avg:
        signal_today = "BUY"
    elif short_avg < long_avg:
        signal_today = "SELL"

    return round(profit, 2), round((profit / prices[0]) * 100, 2), signal_today


def custom_strategy(prices):
    #Buy if price is increasing for last 3 days
    profit = 0
    position = None
    sell_queue = []
    signal_today = None

    for i in range(5, len(prices)):
        price = prices[i]
        increasing = all(prices[i-j] > prices[i-j-1] for j in range(1, 4))

        if increasing:
            if sell_queue:
                sell_price = sell_queue.pop(0)
                profit += sell_price - price
            elif position is None:
                position = price
        elif not increasing:
            if position is not None:
                profit += price - position
                position = None
            else:
                sell_queue.append(price)

    if all(prices[-j] > prices[-j-1] for j in range(1, 4)):
        signal_today = "BUY"
    elif all(prices[-j] < prices[-j-1] for j in range(1, 4)):
        signal_today = "SELL"

    return round(profit, 2), round((profit / prices[0]) * 100, 2), signal_today
