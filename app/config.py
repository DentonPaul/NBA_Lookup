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
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)


configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}