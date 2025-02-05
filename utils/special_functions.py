from yfinance import Ticker  # Type: Ignore


def get_stock_price(stock):
    stock = Ticker(stock)
    price = stock.history(period="1d")["Close"].iloc[0]
    return price
