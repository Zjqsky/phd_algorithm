# -*- coding: UTF-8 -*-
from peewee import *
from app.conf import COMMON_MYSQL
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


class RetryMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    _instance = None

    # 数据库配置
    @staticmethod
    def get_db_instance(host="", port="", database_name="", user="", password="", max_connections=20, stale_timeout=300):
        if not RetryMySQLDatabase._instance:
            RetryMySQLDatabase._instance = RetryMySQLDatabase(
                database_name,
                max_connections=max_connections,
                stale_timeout=stale_timeout,
                host=host,
                user=user,
                password=password,
                port=port
            )
        return RetryMySQLDatabase._instance


COMMON_DB = RetryMySQLDatabase.get_db_instance(**COMMON_MYSQL)


