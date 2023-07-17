# Open SQLAlchemy engine connection and keep its lifecycle #

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI 

engine = create_engine(DATABASE_URI, echo=True)

# Using sessionmaker

Session = sessionmaker(bind=engine)
session = Session()