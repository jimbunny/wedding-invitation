#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/9 2:40 下午
# software: PyCharm

import jwt
from flask import current_app


def generate_jwt(payload, expiry, secret=None):
    """

    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: 生成jwt
    """
    _payload = {'exp': expiry}
    _payload.update(payload)

    if not secret:
        secret = current_app.config['JWT_SECRET']  # 需要在配置文件配置JWT_SECRET

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token.encode().decode()


def verify_jwt(token, secret=None):
    """
    校验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        print(type(token.encode()))
        payload = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        print('-----------')
        print(e)
        payload = None

    return payload

