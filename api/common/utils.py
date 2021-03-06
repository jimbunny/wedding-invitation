#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

import hashlib
import datetime
from .code import CODE_MSG_MAP
import os
import time
import json
from datetime import date, datetime
from flask import jsonify


def pretty_result(code, msg=None, data=None):
    if msg is None:
        msg = CODE_MSG_MAP.get(code)
    if isinstance(data, str):
        return {
            'code': code,
            'msg': msg,
            'data': data
        }
    else:
        return jsonify({
            'code': code,
            'msg': msg,
            'data': data
        })


coverFilePath = r'./downloads/product/cover'
if not os.path.exists(coverFilePath):
    os.makedirs(coverFilePath)

detailFilePath = r'./downloads/product/detail'
if not os.path.exists(detailFilePath):
    os.makedirs(detailFilePath)

descriptionFilePath = r'./downloads/product/description'
if not os.path.exists(descriptionFilePath):
    os.makedirs(descriptionFilePath)


def hash_md5(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()


# 生成订单号
def get_order_code():
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-1:]
    return order_no


def get_zodiac(month, day):
    zodiac = (
        '摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座',
        '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座'
    )
    date = (
        (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
        (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23)
    )
    return zodiac[len(list(filter(lambda x: x <= (month, day), date))) % 12]


def get_age(year, month, day):
    now = datetime.datetime.now()
    now_year, now_month, now_day = now.year, now.month, now.day

    if year >= now_year:
        return 0
    elif month > now_month or (month == now_month and day > now_day):
        return now_year - year - 1
    else:
        return now_year - year


def true_return(data, msg):
    return jsonify({
        "status": True,
        "data": data,
        "msg": msg
    })


def false_return(data, msg):
    return jsonify({
        "status": False,
        "data": data,
        "msg": msg
    })


def create_file(file_path):
    if os.path.exists(file_path):
        print('%s:存在' % file_path)
    else:
        try:
            os.mkdir(file_path)
            print('新建文件夹：%s' % file_path)
        except Exception as e:
            os.makedirs(file_path)
            print('新建多层文件夹：%s' % file_path)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
