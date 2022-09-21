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
    dbUser = os.environ.get('DB_USER')
    dbPassword = os.environ.get('DB_PASSWORD')
    dbServer = os.environ.get('DB_SERVER')
    dbDatabase = os.environ.get('DB_DATABASE')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dbUser}:{dbPassword}@{dbServer}/{dbDatabase}'    
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://b38e624b36920a:4091778d@us-cdbr-east-06.cleardb.net/heroku_f9d43f2f20fae70'    
    #How to make it reconnect?
    
