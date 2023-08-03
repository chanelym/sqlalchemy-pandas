import sys
sys.path.insert(0, '')

from sqlalchemy import text

from database.connector import session

# Use this result to check database connection
# Need to create logging function
result = session.execute(text('SHOW INDEXES FROM alchemy.*;'))
print(result.fetchall())