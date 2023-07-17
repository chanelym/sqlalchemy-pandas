# Database setup. #

from os import environ, path
from dotenv import load_dotenv # Note: never forget to use .env file. Go girl <3 #

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, "../.env"))

# Database connection variables

DATABASE_URI = environ.get("DATABASE_URI")

# Reset data after each run

CLEANUP_DATA = False