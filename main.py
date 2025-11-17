from utils.data_loader import load_csv
from strategies.sma_crossover import sma_crossover
from strategies.ema_crossover import ema_crossover
from backtesting.backtester import Backtester

def main():
    df = load_csv("data/nifty50_ten_year.csv")

    short_window = 50
    long_window = 200

    signal = ema_crossover(df, short_window, long_window)

    bt = Backtester(df, signal)
    bt.run()


if __name__ == "__main__":
    main()