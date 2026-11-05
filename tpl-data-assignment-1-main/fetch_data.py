import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User
from db.models import masked_user
from dataprotection.masking import mask
from config import DATABASE_URL
from config import API_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def main():
    response = requests.get(API_URL)
    users = response.json()
    masked_users = mask(users)

    session = SessionLocal()
    for u in users:
        user = User(
            id=u["id"],
            name=u["name"],
            username=u["username"],
            email=u["email"],
            phone=u["phone"]
        )
        session.merge(user)  # merge avoids duplicate key errors

    for mu in masked_users:
        masked_user_entry = masked_user(
            id=mu["id"],
            name=mu["name"],
            username=mu["username"],
            masked_email=mu["email"],
            masked_phone=mu["phone"]
        )
        session.merge(masked_user_entry)  # merge avoids duplicate key errors
    session.commit()
    session.close()
    print("Users inserted into database.")

if __name__ == "__main__":
    main()