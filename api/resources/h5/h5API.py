#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2021/6/29 下午2:00
# software: PyCharm
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from flasgger import swag_from
from flask import make_response, render_template, abort, request
import json
import os

root = os.path.abspath(os.path.join(os.getcwd()))
headers = {'Content-Type': 'text/html'}


class H5Resource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self, workKey):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        data = {}
        try:
            with open(os.path.join(root, "data", "template", "management.json"), 'r', encoding="utf8") as load_f:
                load_dict = json.load(load_f)
            for item in load_dict.get("data"):
                for key in item:
                    if key == 'key' and item[key] == workKey:
                        data = item
                        break
            if data.get("isTanmu") == 1:
                greetings = []
                path = os.path.join(root, "data", "template", "greetings", str(data.get("id")) + ".txt")
                try:
                    with open(path, mode='r', encoding='utf-8') as ff:
                        greetings = ff.readlines()
                except FileNotFoundError:
                    open(path, 'a').close()
                data['greetings'] = greetings
                return make_response(render_template('index2.html', data=data), 200, headers)
            else:
                return make_response(render_template('index.html', data=data), 200, headers)
        except IndexError:
            abort(404)


class H5ProductResource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self, productKey):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        data = {}
        try:
            with open(os.path.join(root, "data", "template", "product.json"), 'r', encoding="utf8") as load_f:
                load_dict = json.load(load_f)
            for item in load_dict.get("data"):
                for key in item:
                    if key == 'key' and item[key] == productKey:
                        data = item
                        break
            if data.get("isTanmu") == 1:
                greetings = []
                path = os.path.join(root, "data", "template", "greetings", str(data.get("id")) + ".txt")
                try:
                    with open(path, mode='r', encoding='utf-8') as ff:
                        greetings = ff.readlines()
                except FileNotFoundError:
                    open(path, 'a').close()
                data['greetings'] = greetings
                return make_response(render_template('index2.html', data=data), 200, headers)
            else:
                return make_response(render_template('index.html', data=data), 200, headers)
        except IndexError:
            abort(404)


class H5GreetingsResource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])

    def post(self, id):
        """
        test
        :return: json
        """
        # return pretty_result(code.OK)
        # logging.error("error info: %s" % "test error")
        name = request.form.get("name")
        greetings = request.form.get("greetings")
        path = os.path.join(root, "data", "template", "greetings", str(id) + ".txt")
        with open(path, 'a+', encoding="utf8") as f:
            f.write(str(name)+":"+str(greetings) + "\n")
        greetings = []
        f = open(path)  # 返回一个文件对象
        line = f.readline()  # 调用文件的 readline()方法
        while line:
            line = f.readline()
            if line:
                greetings.append(line)
        f.close()
        return pretty_result(code.OK, data=greetings)
