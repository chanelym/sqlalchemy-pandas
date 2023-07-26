import sys
sys.path.insert(0, '')

import pandas as pd

from database.connector import engine

datafile = pd.read_csv('data/categories.csv')
datafile.to_sql(con=engine, name="category", if_exists='replace', index=False)