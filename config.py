import os



class Config:
   QUOTE_API_BASE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
   SECRET_KEY = '123'
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:123@localhost/blogs'
   UPLOADED_PHOTOS_DEST ='app/static/photos'


   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}