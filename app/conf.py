#! /usr/bin/env python
# -*- coding: utf-8 -*-

SERVER_CONF = dict(
    host='0.0.0.0',
    port=9001,
)

COMMON_MYSQL = dict(
    database_name='phd_db',
    host='10.227.69.150',
    port=3306,
    user='dbuser',
    password='dbuser123456',
    max_connections=20,
    stale_timeout=300,
    # cli='mysql -h 10.105.240.128 -u root -P 30306 -proot',
)
