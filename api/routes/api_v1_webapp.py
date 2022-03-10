#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import Blueprint
from flask_restful import Api
from common.code import errors
from resources.webapp import swipes
from resources.webapp import templates

api_v1_webapp = Blueprint('api_v1_webapp', __name__)

api = Api(api_v1_webapp, catch_all_404s=True, serve_challenge_on_401=True, errors=errors)

# #-------------------Mall-----------------------
# swipe management
api.add_resource(swipes.SwipesResource, '/swipes/getList', endpoint='getSwipes')
api.add_resource(swipes.SwipesResource, '/swipes/doEdit', endpoint='editSwipe')

# template management
api.add_resource(templates.TemplatesResource, '/templates/getList', endpoint='getTemplates')
