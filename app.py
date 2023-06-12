import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request

CREATE_CATEGORY_TABLE = (
    "CREATE TABLE IF NOT EXISTS category (id SERIAL PRIMARY KEY, name TEXT);"
)
CREATE_PRODUCT_TABLE = (
    "CREATE TABLE IF NOT EXISTS category (id SERIAL PRIMARY KEY, title TEXT, price FLOAT, category INTEGER, description TEXT, image TEXT);"
)


load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
@app.route("/")
def home():
    return "Hello, Flask!"