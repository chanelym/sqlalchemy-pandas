import sys
sys.path.insert(0, '')

import pandas as pd

from database.connector import engine

tables = ['category', 'customer', 'item', 'orders', 'product']

def createDataFrame(table):
    table_query = f"SELECT \
        TABLE_NAME, COLUMN_NAME, COLUMN_TYPE, COLUMN_KEY, NUMERIC_PRECISION, NUMERIC_SCALE \
            FROM INFORMATION_SCHEMA.COLUMNS \
                WHERE table_name = '{table}' \
                    AND table_schema = 'alchemy'"

    table_df = pd.DataFrame(pd.read_sql_query(table_query, con=engine))
    return table_df

customer_df = createDataFrame("customer")
item_df = createDataFrame("item")
orders_df = createDataFrame("orders")
product_df = createDataFrame("product")

data = pd.concat([category_df, customer_df, item_df, orders_df, product_df])
print(data)