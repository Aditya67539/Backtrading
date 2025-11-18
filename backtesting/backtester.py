import pandas as pd
from backtesting.metrics import compute_metrics

class Backtester:
    def __init__(self, series, signals):
        self.series = series
        self.signals = signals
        self.prices = self.series["Price"]
        self.equity = None

    def run(self, initial_balance=100_000):
        balance = initial_balance
        shares = 0
        invested = False
        equity_curve = []

        for i, signal in enumerate(self.signals):
            price = self.prices.iloc[i]
            
            if not invested and signal == 1:
                shares = balance / price
                invested = True
                balance = 0
                print(f"BUY at price={price}")

            elif invested and signal == -1:
                balance = shares * price
                shares = 0
                invested = False
                print(f"SOLD at price={price}")

            value = balance + shares * price
            equity_curve.append((self.series["Date"].iloc[i], value))
        
        self.equity = pd.Series(
            [v for _, v in equity_curve],
            index = [d for d, _ in equity_curve]
        )

        final_value = balance if not invested else shares * self.prices.iloc[-1]
        pnl = final_value - initial_balance
        print(f"\nTotal invested: {initial_balance}")
        print(f"Final Value: {final_value}")
        print(f"PnL: {pnl}")
        print(f"Percentage: {pnl / initial_balance * 100}")

        compute_metrics(self.equity, initial_balance)

        return self.equity