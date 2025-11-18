import numpy as np

def compute_metrics(equity, initial_balance):
    # CAGR
    print(equity.index[-1], equity.index[0])
    days = (equity.index[-1] - equity.index[0]).days
    years = days / 365
    cagr = (equity.iloc[-1] / initial_balance) ** (1 / years) - 1
    print(f"CAGR: {cagr * 100}%")

    # Sharpe ratio
    daily_returns = equity.pct_change().dropna()

    mean = daily_returns.mean()
    std = daily_returns.std()

    sharpe_ratio = (mean / std) * np.sqrt(252)
    print(f"Sharpe Ratio: {sharpe_ratio}")

    # Max Drawdown
    rolling_max = equity.cummax()
    drawdown = (equity - rolling_max) / rolling_max
    print(f"Max Drawdown: {drawdown.min() * 100}%")