import os

class Config:
    SECRET_KEY = os.urandom(24)

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://omda:omda@localhost:5432/library'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://omda:omda@localhost:5432/library'

config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}