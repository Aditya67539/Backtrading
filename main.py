from utils.data_loader import load_csv

def main():
    df = load_csv("data/nifty50_ten_year.csv")

    print(df)


if __name__ == "__main__":
    main()