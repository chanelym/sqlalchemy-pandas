import sys
sys.path.insert(0, '')

import pandas as pd

from database.connector import engine

# I needed to SET GLOBAL FOREIGN_KEY_CHECKS=0; in order to load the csv files.
# Load the files using the sequence above:

#categories = pd.read_csv('data/categories.csv', sep=',',quotechar='\'',encoding='utf8').set_index('name')
#categories.to_sql('category', con=engine, if_exists='append')

#products = pd.read_csv('data/products.csv', sep=',',quotechar='\'',encoding='utf8', skiprows=[4]).set_index('price')
#products.to_sql('product', con=engine, if_exists='append')

#customers = pd.read_csv('data/customers.csv', sep=',',quotechar='\'',encoding='utf8').set_index('email')
#customers.to_sql('customer', con=engine, if_exists='append')

#items = pd.read_csv('data/items.csv', sep=',', quotechar='\'', encoding='utf8')
#items.to_sql('item', con=engine, if_exists='append', index=False)

#orders = pd.read_csv('data/orders.csv', sep=',', quotechar='\'', encoding='utf8')
#orders.to_sql('orders', con=engine, if_exists='append', index=False)