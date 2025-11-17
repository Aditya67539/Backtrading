from utils.data_loader import load_csv
from indicators.sma import sma
from indicators.ema import ema

def main():
    df = load_csv("data/nifty50_ten_year.csv")

    short_window = 50
    long_window = 200

    short_ema = ema(df["Price"], short_window)
    long_ema = ema(df["Price"], long_window)

    print(long_ema)


if __name__ == "__main__":
    main()