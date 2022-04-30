from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

News = Flask(__name__, instance_relative_config=True)
News.config.from_object(DevConfig)
News.config.from_pyfile('config.py')

bootstrap= Bootstrap(News)

from app import views