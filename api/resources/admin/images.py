#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import Response
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
import os


class ImageResource(Resource):
    """
    示例picture list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        """
            工具函数:
            获取本地图片流
            :param img_local_path:文件单张图片的本地绝对路径
            :return: 图片流
            """
        self.parser.add_argument("id", type=str, location="args", required=True)
        self.parser.add_argument("_type", type=str, location="args", required=True)
        args = self.parser.parse_args()
        img_local_path = os.path.join("./downloads", args._type, str(args.id) + ".png")
        if os.path.exists(img_local_path):
            with open(img_local_path, 'rb') as f:
                image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
        else:
            return pretty_result(code.ERROR, msg='this image not found！')