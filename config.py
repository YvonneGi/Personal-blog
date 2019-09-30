import os



class Config:
    SECRET_KEY = os.urandom(15)

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:123@localhost/blogs'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}