import os

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    mysql_password = "INSERT PASSWORD HERE"
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{mysql_password}@localhost/nba_dev"

class TestConfig(BaseConfig):
    mysql_password = "INSERT PASSWORD HERE"
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{mysql_password}@localhost/nba_test"

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('CLEARDB_DATABASE_URL')

configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}