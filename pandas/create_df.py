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

    dataframe = pd.DataFrame(pd.read_sql_query(table_query, con=engine))
    return dataframe

for eachTable in tables:
    globals()[f'df_{eachTable}'] = createDataFrame(eachTable)

data = pd.concat([df_category, df_customer, df_item, df_orders, df_product])
print(data)