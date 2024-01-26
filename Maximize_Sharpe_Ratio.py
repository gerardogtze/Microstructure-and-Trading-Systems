import numpy as np
import yfinance as yf
from scipy.optimize import minimize
import pandas as pd

def get_asset_returns(ticker):
    aapl_data =  yf.download(ticker,"2023-01-01","2024-01-01")
    adj_close = aapl_data["Adj Close"]
    returns = adj_close.pct_change().dropna()
    return returns
        

def portfolio_data(tickers):
    portfolio_risks = []
    portfolio_returns = []
    all_daily_returns = pd.DataFrame()
    
    for ticker in tickers:
        daily_returns = get_asset_returns(ticker)
        volatility = daily_returns.std()
        portfolio_risks.append(volatility)
        portfolio_returns.append(daily_returns.sum())
        all_daily_returns = pd.concat([all_daily_returns, daily_returns],axis=1 )    
    
    correlation_matrix = all_daily_returns.corr()
    
    return np.array(portfolio_returns), np.array(portfolio_risks), correlation_matrix.values

data = portfolio_data(["AAPL","GOOG", "META"])
print(data)