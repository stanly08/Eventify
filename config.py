import os

class Config:
    m_key = '60ca969c3b2d0a7ec863dd5fdcd3c64e'
    SECRET_KEY = os.environ.get('SECRET_KEY') or m_key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # Set to False in production
