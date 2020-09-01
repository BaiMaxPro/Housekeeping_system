import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.getcwd()

SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or "sqlite:///"
PORT = os.getenv("PORT") or 5000
