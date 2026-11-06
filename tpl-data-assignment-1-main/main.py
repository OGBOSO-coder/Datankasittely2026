from modules.data_analysis import main as analyze_data
from modules.fetch_data import fetch_data


def main():
    fetch_data()
    analyze_data()


if __name__ == "__main__":
    main()