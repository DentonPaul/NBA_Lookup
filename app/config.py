import os

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    
class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

class ProdConfig(BaseConfig):
    try:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    except:
        pass


configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}