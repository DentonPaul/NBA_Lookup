import os

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}