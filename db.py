from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a database engine (SQLite).
engine = create_engine('sqlite:///my_database.db', echo=True)

# Create a session to interact with the database.
Session = sessionmaker(bind=engine)
session = Session()


