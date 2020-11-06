from flask import Flask
import ingredient_analysis_backend.setting as Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
import logging
logging.basicConfig(level=logging.INFO, filename='server.log',filemode='w',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger('log')

db = SQLAlchemy()
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}:{}/{}".format(Config.DB_USER, Config.DB_PASSWORD,
                                                                                Config.DB_HOST, Config.DB_PORT,
                                                                                Config.DB_DBNAME)  # 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(Config.DB_USER,Config.DB_PASSWORD,Config.DB_HOST,Config.DB_PORT,Config.DB_DBNAME)
app.config["SQLALCHEMY_POOL_SIZE"] = Config.SQLALCHEMY_POOL_SIZE
app.config["SQLALCHEMY_POOL_TIMEOUT"] = Config.SQLALCHEMY_POOL_TIMEOUT
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

from ingredient_analysis_backend.controller import uploader
