import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL  # tai voit käyttää suoraan API:sta tullutta sanakirjalistaa

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
    # Vaihtoehto A: Luku suoraan tietokannasta SQLAlchemy-moottorin avulla
    engine = create_engine(DATABASE_URL)
    df = pd.read_sql("SELECT * FROM users", con=engine)
    
    # (Vaihtoehto B: Jos analysoit suoraan aiempaa API-vastausta: df = pd.DataFrame(users))

    analyze_users(df)

if __name__ == "__main__":
    main()