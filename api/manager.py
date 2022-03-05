#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

import os
import logging
import logging.handlers
# from gevent import monkey; monkey.patch_all()
from abc import ABC
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from gunicorn.app.base import BaseApplication
# from gunicorn.six import iteritems
from multiprocessing import cpu_count
from app import create_app, db
from config.setting import config
from logging.handlers import RotatingFileHandler

#  日志级别关系映射
level_relations = {
    'DEBUG':logging.DEBUG,
    'INFO':logging.INFO,
    'WARNING':logging.WARNING,
    'ERROR':logging.ERROR,
    'CRIT':logging.CRITICAL
}

app = create_app(config)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

log_dirs = app.config.get('LOG_DIR_PATH', 'logs')
if not os.path.exists(log_dirs):
    os.makedirs(log_dirs)

formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


# class StandaloneApplication(BaseApplication, ABC):
#     """
#     gunicorn服务器启动类
#     """
#
#     def __init__(self, application, options):
#         self.application = application
#         self.options = options or {}
#         super(StandaloneApplication, self).__init__()
#
#     def load_config(self):
#         config = dict([(key, value) for key, value in iteritems(self.options)
#                        if key in self.cfg.settings and value is not None])
#         for key, value in iteritems(config):
#             self.cfg.set(key.lower(), value)
#
#     def load(self):
#         return self.application


@manager.command
def run():
    """
    生产模式启动命令函数
    To use: python3 manager.py run
    """
    # app.logger.setLevel(app.config.get('LOG_LEVEL', logging.INFO))
    # 日至等级的设置
    logging.basicConfig(level=level_relations.get(app.config.get('LOG_LEVEL', 'INFO')))
    # 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
    file_log_handler = RotatingFileHandler(os.path.join(log_dirs, 'prod.logs'),
                                           maxBytes=app.config.get('LOG_FILE_MAX_BYTES', 1024 * 1024 * 100),
                                           backupCount=app.config.get('LOG_FILE_BACKUP_COUNT', 10))
    # 将日志记录器指定日志的格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

    service_config = {
        'bind': app.config.get('BIND', '0.0.0.0:5678'),
        'workers': app.config.get('WORKERS', cpu_count() * 2 + 1),
        'worker_class': 'gevent',
        'worker_connections': app.config.get('WORKER_CONNECTIONS', 10000),
        'backlog': app.config.get('BACKLOG', 2048),
        'timeout': app.config.get('TIMEOUT', 60),
        'loglevel': app.config.get('LOG_LEVEL', 'info'),
        'pidfile': app.config.get('PID_FILE', 'run.pid'),
    }
    # StandaloneApplication(app, service_config).run()


@manager.command
def debug():
    """
    debug模式启动命令函数
    To use: python3 manager.py debug
    """
    logging.basicConfig(level=level_relations.get(app.config.get('LOG_LEVEL', 'DEBUG')))
    file_log_handler = RotatingFileHandler(os.path.join(log_dirs, 'debug.logs'),
                    maxBytes=app.config.get('LOG_FILE_MAX_BYTES', 1024 * 1024),
                    backupCount=app.config.get('LOG_FILE_BACKUP_COUNT', 1))
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)
    app.run(debug=True, port=5678)


if __name__ == '__main__':
    manager.run()