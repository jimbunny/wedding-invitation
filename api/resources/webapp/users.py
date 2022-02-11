#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/8 10:14 下午
# software: PyCharm

from flask import jsonify, request, current_app, g
from models.appUsers import AppUsersModel
from flask_restful import Resource, inputs
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from common.vaild import password_len
from common.RSA import getRSAtext
from common.decorators import login_required
from config import setting
from werkzeug.datastructures import FileStorage
import os
filePath = r'./downloads/balance/'
if not os.path.exists(filePath):
    os.makedirs(filePath)


class AppUserResource(Resource):
    """
    users list资源类
    """

    def __init__(self):
        self.parser = RequestParser()

    @login_required
    def get(self):
        """
        获取用户信息
        :return: json
        """
        user = AppUsersModel.get(AppUsersModel, g.user_id)
        return pretty_result(code.OK, data=user, msg='get user info successful')

    @login_required
    def post(self):
        user = AppUsersModel.get(AppUsersModel, g.user_id)

        return pretty_result(code.OK, data=user, msg='get user info successful')

    @login_required
    def put(self):
        self.parser.add_argument("email", type=inputs.regex(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'),
                                 required=True, location="json",
                                 help='email format is incorrect')
        self.parser.add_argument("password", type=password_len, location="json", trim=True)
        self.parser.add_argument("description", type=str, location="json", help='description is required')
        args = self.parser.parse_args()
        userEmailInfo = AppUsersModel.query.filter_by(email=args.email).all()
        if userEmailInfo:
            userInfo = AppUsersModel.query.filter_by(email=args.email).first()
            userInfo.description = args.description
            if args.password:
                userInfo.password = AppUsersModel.set_password(AppUsersModel, getRSAtext(args.password))
            AppUsersModel.update(userInfo)
            return pretty_result(code.OK, msg='User info update successful！')
        else:
            return pretty_result(code.ERROR, msg='User info update failed！')


