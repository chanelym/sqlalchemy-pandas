import sys
sys.path.insert(0, '')

import pandas as pd

from database.connector import engine

categories = pd.read_csv('data/categories.csv').to_sql(con=engine, name="category", if_exists='replace', index=False)

customers = pd.read_csv('data/customers.csv').to_sql(con=engine, name="customers", if_exists='replace', index=False)

items = pd.read_csv('data/items.csv').to_sql(con=engine, name="items", if_exists='replace', index=False)

orders = pd.read_csv('data/orders.csv').to_sql(con=engine, name="orders", if_exists='replace', index=False)

products = pd.read_csv('data/products.csv').to_sql(con=engine, name="products", if_exists='replace', index=False)