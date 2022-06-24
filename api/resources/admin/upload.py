#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import Response
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from flask import make_response, render_template, abort, request
import os
import json
import math

root = os.path.abspath(os.path.join(os.getcwd()))
headers = {'Content-Type': 'text/html'}


class UploadTemplateResource(Resource):
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
        try:
            return make_response(render_template('uploadTemplate.html'), 200, headers)
        except Exception as e:
            abort(404)

    def post(self):
        # 获取post过来的文件名称，从name=file参数中获取
        file = request.files['file']
        # secure_filename方法会去掉文件名中的中文
        file_name = 'management.json'
        dirs = os.path.join('data', 'template')
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        file.save(os.path.join('data', 'template', file_name))
        return pretty_result(code.OK)


class UploadSwipeResource(Resource):
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
        try:
            return make_response(render_template('uploadSwipe.html'), 200, headers)
        except Exception as e:
            abort(404)

    def post(self):
        # 获取post过来的文件名称，从name=file参数中获取
        file = request.files['file']
        # secure_filename方法会去掉文件名中的中文
        file_name = 'swipe.json'
        dirs = os.path.join('data', 'template')
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        file.save(os.path.join('data', 'template', file_name))
        return pretty_result(code.OK)


class UploadProductResource(Resource):
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
        try:
            return make_response(render_template('uploadProduct.html'), 200, headers)
        except Exception as e:
            abort(404)

    def post(self):
        # 获取post过来的文件名称，从name=file参数中获取
        file = request.files['file']
        # secure_filename方法会去掉文件名中的中文
        file_name = 'product.json'
        dirs = os.path.join('data', 'template')
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        file.save(os.path.join('data', 'template', file_name))
        return pretty_result(code.OK)


class TemplatesResource(Resource):
    """
    products resource class
    """

    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        """
        get product info
        :return: json
        """
        self.parser.add_argument("pageNo", type=int, required=True, location="args",
                                 help='pageNo is required')
        self.parser.add_argument("pageSize", type=int, required=True, location="args", help='pageSize is required')
        self.parser.add_argument("color", type=str, required=True, location="args", help='color is required')
        args = self.parser.parse_args()

        load_dict = {}
        with open(os.path.join(root, "data", "template", "template.json"), 'r', encoding="utf8") as load_f:
            load_dict = json.load(load_f)
        temp = []
        if args.color == 'all':
            temp = load_dict.get("data")
        for item in load_dict.get("data"):
            if args.color in item.get('tmpColor'):
                temp.append(item)
        origin_list = temp[(args.pageNo-1)*args.pageSize: args.pageNo*args.pageSize]
        result_list = sorted(origin_list, key=lambda e: e.__getitem__('pageViews'))[::-1]
        data = {
            'pageNo': args.pageNo,
            'pageSize': args.pageSize,
            'totalCount': len(temp),
            'totalPages': math.ceil(len(temp)/args.pageSize),
            'items': result_list
        }
        return pretty_result(code.OK, data=data, msg='get template info successful！')
