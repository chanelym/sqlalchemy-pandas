import sys
sys.path.insert(0, '')

from sqlalchemy import text

from database.connector import session

result = session.execute(text('SHOW TABLES;').execution_options(autocommit=True))