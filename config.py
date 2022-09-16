import os
from dotenv import load_dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://garagelab:password123@localhost/dog'
    

class ProductionConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://b38e624b36920a:4091778d@us-cdbr-east-06.cleardb.net/heroku_f9d43f2f20fae70'
    
