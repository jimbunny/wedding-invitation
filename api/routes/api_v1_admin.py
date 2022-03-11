#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm

from flask import Blueprint
from routes.API import Api
from resources.admin import images,upload
from common.code import errors

api_v1_admin = Blueprint('api_v1_admin', __name__)

api = Api(api_v1_admin, catch_all_404s=True, serve_challenge_on_401=True, errors=errors)

# image
api.add_resource(images.ImageResource, '/image', endpoint='getImage')
api.add_resource(upload.UploadTemplateResource, '/template', endpoint='getTemplateFile')
api.add_resource(upload.UploadTemplateResource, '/template/uploader', endpoint='postTemplateFile')
api.add_resource(upload.UploadSwipeResource, '/swipe', endpoint='getSwipeFile')
api.add_resource(upload.UploadSwipeResource, '/swipe/uploader', endpoint='postSwipeFile')
