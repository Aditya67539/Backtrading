class Backtester:
    def __init__(self, series, signals):
        self.series = series
        self.signals = signals
        self.prices = self.series["Price"]

    def run(self, initial_balance=100_000):
        balance = initial_balance
        shares = 0
        invested = False
        total_invested = 0

        for i, signal in enumerate(self.signals):
            price = self.prices[i]
            
            if not invested and signal == 1:
                shares = balance / price
                total_invested += balance
                invested = True
                balance = 0
                print(f"BUY at price={price}")

            elif invested and signal == -1:
                balance = shares * price
                shares = 0
                invested = False
                print(f"SOLD at price={price}")

        final_value = balance if not invested else shares * self.prices[0]
        pnl = final_value - total_invested
        print(f"Total invested: {total_invested}")
        print(f"Final Value: {final_value}")
        print(f"PnL: {pnl}")
        print(f"Percentage: {pnl / total_invested * 100}")