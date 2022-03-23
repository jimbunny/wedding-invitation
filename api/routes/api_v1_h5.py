#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import Blueprint
from flask_restful import Api
from common.code import errors
from resources.h5 import h5API

api_v1_h5 = Blueprint('api_v1_h5', __name__)

api = Api(api_v1_h5, catch_all_404s=True, serve_challenge_on_401=True, errors=errors)

api.add_resource(h5API.H5Resource, '/work/<workKey>', endpoint='work')
api.add_resource(h5API.H5ProductResource, '/product/<productKey>', endpoint='product')
api.add_resource(h5API.H5GreetingsResource, '/greetings/<id>', endpoint='tanmu')
api.add_resource(h5API.H5ViewResource, '/<_type>/<view_type>/<h5Key>', endpoint='h5Template')
api.add_resource(h5API.MakeH5TemplateResource, '/makeH5/<_type>/<h5Key>', endpoint='makeH5Template')
