from asyncio.log import logger
from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    
    IMMUDB_HOST: str = os.environ.get('DEV_IMMUDB_HOST')
    IMMUDB_PORT: str = os.environ.get('DEV_IMMUDB_PORT')
    IMMUDB_DB: str = os.environ.get('DEV_IMMUDB_DB')
    IMMUDB_USER: str = os.environ.get('DEV_IMMUDB_USER')
    IMMUDB_PASSWORD: str = os.environ.get('DEV_IMMUDB_PASSWORD')
        
class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    IMMUDB_HOST: str = os.environ.get('IMMUDB_HOST')
    IMMUDB_PORT: str = os.environ.get('IMMUDB_PORT')
    IMMUDB_DB: str = os.environ.get('IMMUDB_DB')
    IMMUDB_USER: str = os.environ.get('IMMUDB_USER')
    IMMUDB_PASSWORD: str = os.environ.get('IMMUDB_PASSWORD')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app];