import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.getcwd()

SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or "sqlite:///"
PORT = os.getenv("PORT") or 5000

FLASK_ENV = os.getenv("FLASK_ENV") or "production"

DEBUG = FLASK_ENV == "debug"

INIT_DATABASE = os.getenv("FLASK_INIT_DATABASE") == 'true'
