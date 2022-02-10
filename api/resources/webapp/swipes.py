#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/7 10:14 下午
# software: PyCharm


from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from common import code, pretty_result
import os
from config.setting import config
from werkzeug.datastructures import FileStorage

filePath = r'./downloads/swipe/'
if not os.path.exists(filePath):
    os.makedirs(filePath)


class SwipesResource(Resource):
    """
    swipe list资源类
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
        data = []
        for i in os.listdir(filePath):
            url = config.domain + "/api/v1/admin/image?_type=swipe&id=" + i.split(".")[0]
            data.append({"name": i, "url": url, "carouselUrl": url})
        return pretty_result(code.OK, data=data, msg='Get swipes picture successful！')

    def put(self):
        """
            工具函数:
            获取本地图片流
            :param img_local_path:文件单张图片的本地绝对路径
            :return: 图片流
            """
        self.parser.add_argument("picture", type=FileStorage, location='files', action='append',
                                 help='picture is required')
        self.parser.add_argument("removeList", type=str, required=True, location="form", help='removelist is required')
        args = self.parser.parse_args()
        removeList = args.removeList.split(",")
        if args.picture:
            for item in args.picture:
                if item.filename in removeList:
                    continue
                new_fname = filePath + str(item.filename) + '.png'
                item.save(new_fname)
        for i in os.listdir(filePath):
            if i in removeList:
                old_fname = filePath + i
                if os.path.exists(old_fname):
                    os.remove(old_fname)
                else:
                    print(str(i) + " the file does not exist")
        return pretty_result(code.OK, msg='Update swipes picture successful！')
