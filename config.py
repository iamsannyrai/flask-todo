import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    TESTING = False
    DEBUG = True


class DevelopmentConfig(Config):
    ENV = "development"
    pass


class TestingConfig:
    ENV = "testing"
    TESTING = True


class ProductionConfig:
    DEBUG = False
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
