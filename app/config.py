import os

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{os.getenv('mysql_password')}@localhost/dev"

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{os.getenv('mysql_password')}@localhost/test"

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}