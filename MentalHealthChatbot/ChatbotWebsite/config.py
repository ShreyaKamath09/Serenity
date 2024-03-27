import os
import secrets
import string

def generate_secret_key(length=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

SECRET_KEY = generate_secret_key()

class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # contain mysql database url with user and password
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your-database-file.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/users' #mysql
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  #Alternative database if mysql not working
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("Serene Team")
    MAIL_PASSWORD = os.environ.get("sereneMPR6")
