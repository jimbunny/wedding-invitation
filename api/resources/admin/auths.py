#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/8 10:14 下午
# software: PyCharm
from datetime import datetime, timedelta
from flask_restful import Resource
from common.jwt_util import generate_jwt
import jwt, datetime, time
from flask import current_app, g
from models.adminUsers import AdminUsersModel
from common import code, pretty_result
from datetime import datetime


class AuthorizationResource(Resource):
    """
    登录认证
    """
    @staticmethod
    def _generate_tokens(user_id, with_refresh_token=True):
        """
        生成token 和refresh_token
        :param user_id: 用户id
        :return: token, refresh_token
        """
        #  颁发JWT
        now = datetime.utcnow()
        expiry = now + timedelta(hours=current_app.config['JWT_EXPIRY_HOURS'])  # 短期token
        # expiry = now + timedelta(seconds=10)
        token = generate_jwt({'user_id': user_id, 'refresh': False}, expiry)
        refresh_token = None
        if with_refresh_token:
            refresh_expiry = now + timedelta(days=current_app.config['JWT_REFRESH_DAYS'])  # 长期token
            # refresh_expiry = now + timedelta(seconds=20)  # 长期token
            refresh_token = generate_jwt({'user_id': user_id, 'refresh': True}, refresh_expiry)
        return token, refresh_token

    def post(self, username, password):
        """
        用户登录创建token
        """
        userInfo = AdminUsersModel.query.filter_by(username=username).first()
        if (userInfo is None):
            return pretty_result(code.ERROR, data='', msg='User is not exit!')
        else:
            if (userInfo.check_password(password)):
                login_time = datetime.now()
                print(login_time)
                userInfo.login_time = login_time
                AdminUsersModel.update(userInfo)
                user_id = userInfo.id
                token, refresh_token = self._generate_tokens(user_id)
                return pretty_result(code.OK, data={'access_token': token, 'refresh_token': refresh_token},
                                     msg='Login successful!')
            else:
                return pretty_result(code.ERROR, data='', msg='Password is not correct!')

    # 补充put方式 更新token接口
    def put(self):
        """
        刷新token
        """
        user_id = g.user_id
        if user_id and g.is_refresh_token:
            token, refresh_token = self._generate_tokens(user_id, with_refresh_token=False)
            return pretty_result(code.OK, data={'access_token': token})
        else:
            return pretty_result(code.AUTHORIZATION_ERROR, data='', msg='Wrong refresh token.')


# 没用refresh重刷机制
class AuthResource(Resource):
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'jim',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                # config.SECRET_KEY,
                current_app.config.get('SECRET_KEY', ''),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            # 取消过期时间验证
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY', ''), options={'verify_exp': False})
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token expired!'
        except jwt.InvalidTokenError:
            return 'Invalid token!'


    def authenticate(self, username, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
        :param password:
        :return: json
        """
        userInfo = AdminUsersModel.query.filter_by(username=username).first()
        if (userInfo is None):
            return pretty_result(code.OK, data='', msg='User is not exit!')
        else:
            if (AdminUsersModel.check_password(AdminUsersModel, userInfo.password, password)):
                login_time = int(time.time())
                userInfo.login_time = login_time
                AdminUsersModel.update(AdminUsersModel)
                token = self.encode_auth_token(userInfo.id, login_time)
                return pretty_result(code.OK, data=token.decode(), msg='Login successful!')
            else:
                return pretty_result(code.OK, data='', msg='Password is not correct!')

    def identify(self, request):
        """
        用户鉴权
        :return: list
        """
        data = ''
        msg = ''
        status = code.AUTHORIZATION_ERROR
        auth_header = request.headers.get('Authorization')
        if (auth_header):
            auth_tokenArr = auth_header.split(" ")
            if (not auth_tokenArr or auth_tokenArr[0] != 'JWT' or len(auth_tokenArr) != 2):
                msg = 'Please pass the correct authentication header information!'
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = AdminUsersModel.get(AdminUsersModel, payload['data']['id'])
                    if (user is None):
                        msg = 'User is not exit!'
                    else:
                        if (user.login_time == payload['data']['login_time']):
                            status = code.OK
                            data = user.id
                            msg = 'Request successful!'
                        else:
                            msg = 'Token has been changed, please log in again to obtain!'
                else:
                    msg = payload
        else:
            msg = 'No authentication token provided'
        return pretty_result(status, data=data, msg=msg)
