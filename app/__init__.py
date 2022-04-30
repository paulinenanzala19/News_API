from flask import Flask
from .config import DevConfig

News = Flask(__name__, instance_relative_config=True)
News.config.from_object(DevConfig)
News.config.from_pyfile('config.py')

from app import views