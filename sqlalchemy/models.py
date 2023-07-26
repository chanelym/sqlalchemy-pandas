import sys
sys.path.insert(0, '')

from sqlalchemy import Column, Date, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from database.connector import engine, session

Base = declarative_base()

# I'm using alchemy database from MySQL.
# Now, I want to create tables

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'Category {self.name}'

Base.metadata.create_all(engine)