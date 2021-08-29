# -*- coding: UTF-8 -*-
import json
from functools import wraps
from utils.api import Response, ApiStatusCode
import logging
import traceback
from flask import request


# api装饰器
def api(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        try:
            # 打印日志
            logging.info('request: {"args": %s, "kwargs": %s}' % (str(args), str(kwargs)))
            ret = function(*args, **kwargs)
        except Exception as e:
            logging.error('%s\n request: {"args": %s, "kwargs": %s}' % (traceback.format_exc(), str(args), str(kwargs)))
            ret = Response(message=str(e), status=ApiStatusCode.error.value)
        ret = ret.__dict__
        logging.info('response: %s' % (str(ret)))

        return json.dumps(ret)

    return decorator


# api接口参数验证装饰器
def validate(*fields):
    def decorator(function):
        @wraps(function)
        def wrap(*args, **kwargs):
            params = {}
            for field in fields:
                v = field.validate()
                params[field.name] = v
            kwargs.update(params)
            return function(*args, **kwargs)

        return wrap

    return decorator


# 接口参数规范定义
class Field(object):
    def __init__(self, name, _type, default=None, required=False,
                 func=lambda x: True, trim=False, available=None, limit=None):
        self.name = name
        self._type = _type
        self.default = default
        self.required = required
        self.func = func
        self.value = self.default
        self.trim = trim
        self.available = available
        self.limit = limit

    def validate(self):
        arg_value = request.args.get(self.name, None)
        form_value = request.form.get(self.name, None)
        json_value = load_json(request.data).get(self.name, None) if request.data != b'' else None

        value = json_value if json_value is not None else (
            form_value if form_value is not None else (
                arg_value if arg_value is not None else None
            )
        )

        # 为空取默认值，不为空进行格式转化
        if value is not None:
            try:
                if self._type == 'json_str':
                    value = json.dumps(value)
                else:
                    value = self._type(value)
            except Exception as e:
                value = self.default
        elif self.default is not None and not self.required:
            value = self.default

        # 去无用字符
        if self.trim is True and isinstance(value, str):
            value = value.strip()

        # 是否必须
        if self.required is True and value is None:
            raise Exception('缺少参数：{}'.format(self.name))

        # 经函数处理
        if self.func(value) is False:
            raise Exception('参数 {} 未经过验证'.format(self.name))

        # 是否非法参数
        if self.available is not None and value is not None and value not in self.available:
            raise Exception('非法的参数值 {} '.format(self.name))

        # 范围限制
        if self.limit is not None and (
                (self.limit[0] is not None and value < self.limit[0]) or (
                self.limit[1] is not None and value > self.limit[0])):
            raise Exception('非法的参数值 {} '.format(self.name))

        if value is not None:
            return value

        return None


# json参数转化
def load_json(json_val):
    try:
        json_object = json.loads(json_val)
    except Exception as e:
        return {}
    return json_object



