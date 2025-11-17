from utils.data_loader import load_csv
from indicators.sma import sma

def main():
    df = load_csv("data/nifty50_ten_year.csv")

    short_window = 50
    long_window = 200

    short_sma = sma(df["Price"], short_window)
    long_sma = sma(df["Price"], long_window)

    print(long_sma)


if __name__ == "__main__":
    main()