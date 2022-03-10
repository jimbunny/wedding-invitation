#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2020/6/8 10:14 下午
# software: PyCharm

from flask_restful.reqparse import RequestParser
from common import code, pretty_result
from flask_restful import Resource
import json
import os
root = os.path.abspath(os.path.join(os.getcwd()))


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
        self.parser.add_argument("name", type=str, required=True, location="args", help='name is required')
        args = self.parser.parse_args()
        # template_list = TemplatesModel.filter_by_name(TemplatesModel, name=args.name)
        # items = []
        # for template in template_list:
        #     tmp = template.to_dict()
        #     tmp['url'] = config.domain + "/api/v1/admin/image?_type=template&id=" + template.name
        #     items.append(tmp)
        # data = {
        #     'pageNo': args.pageNo,
        #     'pageSize': args.pageSize,
        #     'totalCount': len(template_list),
        #     'items': items
        # }
        load_dict = {}
        with open(os.path.join(root, "data", "template", "management.json"), 'r', encoding="utf8") as load_f:
            load_dict = json.load(load_f)
        return pretty_result(code.OK, data=load_dict, msg='get template info successful！')
