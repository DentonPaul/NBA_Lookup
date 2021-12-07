import os

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    
class DevConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SQLALCHEMY_DATABASE_URI = "mysql://root:Turtleturtle7!@localhost/nba_dev"
    

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql://root:Turtleturtle7!@localhost/nba_test"

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