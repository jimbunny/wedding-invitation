#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2021/6/29 下午2:00
# software: PyCharm
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from flask import make_response, render_template, abort, jsonify
import json
import os
root = os.path.abspath(os.path.join(os.getcwd()))
headers = {'Content-Type': 'text/html'}


class TestResource(Resource):
    """
    test list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        """
        获取用户信息
        :return: json
        """
        # return pretty_result(code.OK)
        data = {}
        try:
            with open(os.path.join(root, "data", "template", "management.json"), 'r', encoding="utf8") as load_f:
                load_dict = json.load(load_f)
            for item in load_dict.get("data"):
                for key in item:
                    if key == 'key' and item[key] == 'H5t8so51148n':
                        data = item
                        break
            greetings = []
            path = os.path.join(root, "data", "template", "greetings", str(data.get("id")) + ".txt")
            f = open(path)  # 返回一个文件对象
            line = f.readline()  # 调用文件的 readline()方法
            while line:
                line = f.readline()
                if line:
                    greetings.append(line)
            f.close()
            data['greetings']=greetings
            if data.get("isTanmu") == 1:
                return make_response(render_template('index2.html', data=data), 200, headers)
            else:
                return make_response(render_template('index.html', data=data), 200, headers)
        except IndexError:
            abort(404)

    def post(self):
        """
        获取用户信息
        :return: json
        """
        return pretty_result(code.OK)
