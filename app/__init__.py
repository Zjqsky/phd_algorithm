from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)  # 创建一个wsgi应用

# 设置日志的格式       日志等级       日志信息的文件名　　行数　　日志信息
log_format = '%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d - %(message)s'
# 日志的等级的设置
logging.basicConfig(format=log_format, level=logging.DEBUG)
# 创建日志记录器，　指明日志保存的路径
file_log_handler = RotatingFileHandler('logs/log.txt')
# 文件日志格式化
formatter = logging.Formatter(log_format)
# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)

