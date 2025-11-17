from utils.data_loader import load_csv
from strategies.sma_crossover import sma_crossover

def main():
    df = load_csv("data/nifty50_ten_year.csv")

    short_window = 50
    long_window = 200

    sma_crossover(df, short_window, long_window)


if __name__ == "__main__":
    main()