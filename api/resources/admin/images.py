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
from werkzeug.utils import secure_filename
import os
root = os.path.abspath(os.path.join(os.getcwd()))
headers = {'Content-Type': 'text/html'}


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


class UploadImageResource(Resource):
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
            return make_response(render_template('uploadImages.html'), 200, headers)
        except Exception as e:
            abort(404)

    def post(self):
        # 获取post过来的文件名称，从name=file参数中获取
        file = request.files['file']
        # secure_filename方法会去掉文件名中的中文
        filename = secure_filename(file.filename)
        dirs = os.path.join(root, 'downloads', 'template')
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        file.save(os.path.join(root, 'downloads', 'template', filename))
        return pretty_result(code.OK)