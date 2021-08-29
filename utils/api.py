# -*- coding: UTF-8 -*-
from enum import Enum, unique


# api返回状态吗
@unique
class ApiStatusCode(Enum):
    ok = 0
    error = -1


# api返回接口格式
class Response(object):
    def __init__(self, data=None, message="", status=ApiStatusCode.ok.value):
        self.data = data
        self.message = message
        self.status = status


