from logging.handlers import RotatingFileHandler

from flask import Flask
from config import config
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import redis
from config import Config
import logging


db = SQLAlchemy()


def setup_log(config_name):
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):

    setup_log(config_name)
    app = Flask(__name__)
    CSRFProtect(app)
    db.init_app(app)
    app.config['SESSION_USE_SIGNER'] = Config.SESSION_USE_SIGNER
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    from info.model.index import index
    app.register_blueprint(index)
    global redis_store
    redis_store = redis.StrictRedis(Config.REDIS_HOST, Config.REDIS_PORT)
    app.config.from_object(config[config_name])
    Session(app)
    return app

