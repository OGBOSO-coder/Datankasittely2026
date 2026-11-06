import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

def analyze_users(df: pd.DataFrame):
    print("--- Datan muoto (rivit, sarakkeet) ---")
    print(df.shape)
    print()

    print("--- Kaksi ensimmäistä riviä ---")
    print(df.head(2))
    print()

    print("--- Kaksi viimeistä riviä ---")
    print(df.tail(2))
    print()

def main():
    engine = create_engine(DATABASE_URL)
    df = pd.read_sql("SELECT * FROM users", con=engine)


    analyze_users(df)

if __name__ == "__main__":
    main()