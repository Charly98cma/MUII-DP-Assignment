import pandas as pd


def main():
    # Read CSV
    df = pd.read_csv('COVID19_data.csv', sep=',', header=0, index_col='ID')


if __name__ == "__main__":
    main()
