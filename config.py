# config.py
import os

class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # SQLite URI
