# -*- coding: UTF-8 -*-
from app import app, conf

# 配置路由，不能删
import urls

if __name__ == '__main__':
    app.run(debug=True, host=conf.SERVER_CONF['host'], port=conf.SERVER_CONF['port'])

