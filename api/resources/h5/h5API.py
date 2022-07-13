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
from config.h5Template.templateBtn import templateBtn
from config.h5Template.tanmuContent import tanmuContent
from config.h5Template.payContent import payContent
from config.h5Template.titleLink import titleLink
from config.h5Template.phone import phone
from config.h5Template.pc import pc

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
                return make_response(render_template('index_bak.html', data=data), 200, headers)
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
                return make_response(render_template('index_bak.html', data=data), 200, headers)
        except IndexError:
            abort(404)


class H5FormResource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self, id):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        data = {"presents": "", "greetings": "", "isTanmu": 0, "isPresent": 0}
        try:
            isTanmu = 0
            isPresent = 0
            if int(id) >= 10000:
                with open(os.path.join(root, "data", "template", "product.json"), 'r', encoding="utf8") as load_f:
                    load_dict2 = json.load(load_f)
            else:
                with open(os.path.join(root, "data", "template", "template.json"), 'r', encoding="utf8") as load_f:
                    load_dict2 = json.load(load_f)
            for item in load_dict2.get("data"):
                for key in item:
                    if key == 'id' and item["id"] == str(id):
                        pretty_result(item["id"])
                        isTanmu = item["isTanmu"]
                        isPresent = item["isPresent"]
                        data["isPresent"] = int(isPresent)
                        data["isTanmu"] = int(isTanmu)
            greetingPath = os.path.join(root, "data", "template", "greetings", str(id) + ".json")
            presentPath = os.path.join(root, "data", "template", "presents", str(id) + ".json")
            if not isTanmu and not isPresent:
                abort(404)
            present = {'data': []}
            if data["isPresent"] and not os.path.exists(presentPath):
                json_str = json.dumps(present, indent=4)
                with open(presentPath, 'w') as json_file:
                    json_file.write(json_str)
            greeting = {'data': []}
            print(data["isTanmu"])
            if data["isTanmu"] and not os.path.exists(greetingPath):
                json_str = json.dumps(greeting, indent=4)
                with open(greetingPath, 'w') as json_file:
                    json_file.write(json_str)

            with open(greetingPath, 'r', encoding="utf8") as load_f:
                load_dict = json.load(load_f)
                data["greetings"] = load_dict
            with open(presentPath, 'r', encoding="utf8") as load_f:
                load_dict = json.load(load_f)
                data["presents"] = load_dict

            return make_response(render_template('form.html', data=data), 200, headers)
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

    def get(self, id):
        greetings = {'data': []}
        path = os.path.join(root, "data", "template", "greetings", str(id) + ".json")
        if not os.path.exists(path):
            json_str = json.dumps(greetings, indent=4)
            with open(path, 'w') as json_file:
                json_file.write(json_str)
        with open(path, 'r', encoding="utf8") as load_f:
            load_dict = json.load(load_f)
        return pretty_result(code.OK, data=load_dict.get('data'))

    def post(self, id):
        """
        test
        :return: json
        """
        # return pretty_result(code.OK)
        # logging.error("error info: %s" % "test error")
        name = request.form.get("name")
        greetings = request.form.get("greetings")
        path = os.path.join(root, "data", "template", "greetings", str(id) + ".json")
        with open(path, 'r', encoding="utf8") as load_f:
            load_dict = json.load(load_f)
        load_dict.get('data').append({"text":str(name)+":"+str(greetings)})
        json_str = json.dumps(load_dict, indent=4)
        with open(path, 'w') as json_file:
            json_file.write(json_str)
        return pretty_result(code.OK, data=str(str(name)+":"+str(greetings)))


class H5PresentResource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])

    def get(self, id):
        present = {'data': []}
        path = os.path.join(root, "data", "template", "presents", str(id) + ".json")
        if not os.path.exists(path):
            json_str = json.dumps(present, indent=4)
            with open(path, 'w') as json_file:
                json_file.write(json_str)
        with open(path, 'r', encoding="utf8") as load_f:
            load_dict = json.load(load_f)
        return pretty_result(code.OK, data=load_dict.get('data'))

    def post(self, id):
        """
        test
        :return: json
        """
        # return pretty_result(code.OK)
        # logging.error("error info: %s" % "test error")
        name = request.form.get("name")
        present = request.form.get("present")
        path = os.path.join(root, "data", "template", "presents", str(id) + ".json")
        presentInit = {'data': []}
        if not os.path.exists(path):
            json_str = json.dumps(presentInit, indent=4)
            with open(path, 'w') as json_file:
                json_file.write(json_str)

        with open(path, 'r', encoding="utf8") as load_f:
            load_dict = json.load(load_f)
        load_dict.get('data').append({"name": str(name), "number": str(present)})
        json_str = json.dumps(load_dict, indent=4)
        with open(path, 'w') as json_file:
            json_file.write(json_str)
        return pretty_result(code.OK)


class H5ViewResource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self, view_type, _type, h5Key):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        data = {}
        with open(os.path.join(root, "data", "template", str(_type) + ".json"), 'r', encoding="utf8") as load_f:
            load_dict = json.load(load_f)
        for item in load_dict.get("data"):
            for key in item:
                if key == 'key' and item[key] == h5Key[:18]:
                    data = item
                    break
        if data.get("isTanmu") == 1:
            greetings = {"data": [{"text": "Unika:ขออวยพรให้คุณมีความสุขตลอดไป."}]}
            path = os.path.join(root, "data", "template", "greetings", str(data.get("id")) + ".json")
            if not os.path.exists(path):
                json_str = json.dumps(greetings, indent=4)
                with open(path, 'w') as json_file:
                    json_file.write(json_str)
            try:
                with open(path, 'r', encoding="utf8") as load_f:
                    load_dict = json.load(load_f)
                    greetings = load_dict.get('data')
            except FileNotFoundError:
                open(path, 'a').close()
                # json_str = json.dumps(greetings)
                # with open(path, 'w') as json_file:
                #     json_file.write(json_str)
            data['greetings'] =greetings
        try:
            if view_type == "pc":
                htmlPath = str(_type) + '/' + str(h5Key) + '_pc.html'
            else:
                htmlPath = str(_type) + '/' + str(h5Key) + '.html'
            return make_response(render_template(htmlPath, data=data), 200, headers)
        except IndexError:
            abort(404)


class MakeH5TemplateResource(Resource):
    """
    test list资源类
    """

    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    def gen_h5(self, _type, h5Key, data):
        try:
            import requests
            pcHeader = {
                'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
            phoneHeader = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'}

            pcUrl = 'https://maka.im/pcviewer/601736963/' + str(h5Key)
            phoneUrl = 'https://maka.im/viewer/601736963/' + str(h5Key)
            pcHtml = requests.get(pcUrl, headers=pcHeader)
            phoneHtml = requests.get(phoneUrl, headers=phoneHeader)
            pcHtml.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
            phoneHtml.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
            pcUrl = "https://www.uniecard.com/pcViewer/" + _type + "/" + str(h5Key)
            phoneUrl = "https://www.uniecard.com/viewer/" + _type + "/" + str(h5Key)
            path = os.path.join(root, "templates")

            # font
            IsPc = pc(phoneUrl, data.get('font'))
            IsPhone = phone(pcUrl, data.get('font'))
            phoneIndex = phoneHtml.text.find('<body>')
            pcIndex = pcHtml.text.find('<body>')
            phoneHtml = phoneHtml.text[:phoneIndex + 6] + IsPhone + phoneHtml.text[phoneIndex + 6:]
            pcHtml = pcHtml.text[:pcIndex + 6] + IsPc + pcHtml.text[pcIndex + 6:]

            phoneHtml = phoneHtml.replace("https://img1.maka.im/favicon.ico","https://www.uniecard.com/static/favicon.ico").replace('class="mark"', '')
            pcHtml = pcHtml.replace("https://img1.maka.im/favicon.ico","https://www.uniecard.com/static/favicon.ico").replace(
                "打开微信", "เปิด Line/Facebook").replace("点击 发现 扫一扫 扫描二维码 可在手机上预览该h5页面","สแกนคิวอาร์โค๊ด เพื่อแสดงผลบนโทรศัพท์"). \
                replace('<img class="pcviewer-infoarea-qrcodearea-img"/>','<canvas class="pcviewer-infoarea-qrcodearea-img" id="qrcode-canvas"></canvas>'). \
                replace('src="//maka.im/viewer/601736963', 'src="https://www.uniecard.com/viewer/'+_type).replace(
                'class="mark"', '')

            if data.get("isFunction") or data.get("isTanmu"):
                phoneIndex = phoneHtml.find('</title>')
                phoneHtml = (phoneHtml[:phoneIndex + 8] +
                                             titleLink + phoneHtml[phoneIndex + 8:])

            # function
            # if data.get("isFunction"):
            #     phoneIndex = phoneHtml.find('</html>')
            #     payContentNew = payContent(template_type=data.get("_type"))
            #     phoneHtml = phoneHtml[:phoneIndex] + payContentNew + phoneHtml[phoneIndex:]

            # tanmu
            if data.get("isTanmu"):
                phoneIndex = phoneHtml.find('</html>')
                tanmuContentNew = tanmuContent(template_type=data.get("_type"))
                phoneHtml = phoneHtml[:phoneIndex] + tanmuContentNew + phoneHtml[phoneIndex:]

            path = os.path.join(path, str(_type))
            if not os.path.exists(path):
                os.makedirs(path)
            filePathPhonePath = os.path.join(path, str(h5Key) + ".html")
            filePathPhone = open(filePathPhonePath, "w", encoding="utf-8")
            filePathPcPath = os.path.join(path, str(h5Key) + "_pc.html")
            filePathPc = open(filePathPcPath, "w", encoding="utf-8")

            filePathPhone.write(phoneHtml)
            filePathPhone.close()
            filePathPc.write(pcHtml)
            filePathPc.close()

            if _type == "template":
                filePathPhoneBtn = os.path.join(path, str(h5Key) + "_btn" + ".html")
                filePathPcBtn = os.path.join(path, str(h5Key) + "_btn_pc" + ".html")
                phoneIndex = phoneHtml.find('<body>')
                # pcIndex = pcHtml.find('<body>')
                phoneBtnHtml = phoneHtml[:phoneIndex + 6] + templateBtn + phoneHtml[phoneIndex + 6:]
                # pcBtnHtml = pcHtml[:pcIndex + 6] + pcHtml[pcIndex + 6:]
                phoneBtnFile = open(filePathPhoneBtn, "w", encoding="utf-8")
                # pcBtnFile = open(filePathPcBtn, "w", encoding="utf-8")
                phoneBtnFile.write(phoneBtnHtml)
                phoneBtnFile.close()
                # pcBtnFile.write(pcBtnHtml)
                # pcBtnFile.close()

            return True, [phoneUrl, pcUrl]
        except Exception as e:
            print(e)
            return False, ""

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self, _type, h5Key):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        # http://maka.im/viewer/601736963/1CKXBVN2W601736963

        # https://u601736963.viewer.maka.im/k/1CKXBVN2W601736963


        if h5Key != 'all':
            with open(os.path.join(root, "data", "template", str(_type)+".json"), 'r', encoding="utf8") as load_f:
                load_dict = json.load(load_f)
            for item in load_dict.get("data"):
                for key in item:
                    if key == 'key' and item[key] == h5Key:
                        data = item
                        break
            status, data = self.gen_h5(_type, h5Key, data)
            if not status:
                return pretty_result(code.ERROR, data=data, msg=str(_type) + "---" + str(h5Key) + '  make h5 failed！')
            return pretty_result(code.OK, data=data, msg='make h5 successful！')
        else:
            with open(os.path.join(root, "data", "template", str(_type)+".json"), 'r',
                      encoding="utf8") as load_f:
                load_dict = json.load(load_f)
            for item in load_dict.get("data"):
                status, data = self.gen_h5(_type, item.get('key'), item)
                if not status:
                    return pretty_result(code.ERROR, data=data, msg=str(_type) + "---" + str(h5Key) + '  make h5 failed！')
            return pretty_result(code.OK, msg='make h5 successful！')


class MakeH5TemplateResource2(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self, _type, h5Key):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        # http://maka.im/viewer/601736963/1CKXBVN2W601736963

        # https://u601736963.viewer.maka.im/k/1CKXBVN2W601736963

        import requests

        pcHeader = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
        phoneHeader = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'}

        pcUrl = 'https://maka.im/pcviewer/601736963/' + str(h5Key)
        phoneUrl = 'https://maka.im/viewer/601736963/' + str(h5Key)
        pcHtml = requests.get(pcUrl, headers=pcHeader)
        phoneHtml = requests.get(phoneUrl, headers=phoneHeader)
        pcHtml.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
        phoneHtml.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
        pcUrl = "https://www.uniecard.com/pcViewer/" + _type + "/" + str(h5Key)
        phoneUrl = "https://www.uniecard.com/viewer/" + _type + "/" + str(h5Key)

        path = os.path.join(root, "templates")

        # phoneFinalString = (phoneHtml.text[:phoneIndex + 6] + IsPhone + templateBtn + phoneHtml.text[phoneIndex + 6:])
        # pcFinalString = (pcHtml.text[:pcIndex + 6] + IsPc + pcHtml.text[pcIndex + 6:])


        if h5Key != 'all':
            try:
                if _type == 'template':
                    with open(os.path.join(root, "data", "template", "management.json"), 'r', encoding="utf8") as load_f:
                        load_dict = json.load(load_f)
                    for item in load_dict.get("data"):
                        for key in item:
                            if key == 'key' and item[key] == h5Key:
                                data = item
                                break
                    IsPc = pc(phoneUrl, data.get('font'))
                    IsPhone = phone(pcUrl, data.get('font'))
                    phoneIndex = phoneHtml.text.find('<body>')
                    pcIndex = pcHtml.text.find('<body>')
                    path = os.path.join(root, "templates")
                    phoneFinalString = (phoneHtml.text[:phoneIndex + 6] + IsPhone + templateBtn + phoneHtml.text[phoneIndex + 6:])
                    pcFinalString = (pcHtml.text[:pcIndex + 6] + IsPc + pcHtml.text[pcIndex + 6:])
                    if data.get("isTanmu"):
                        phoneFinalStringIndex = phoneFinalString.find('</title>')
                        # pcFinalStringIndex = pcFinalString.find('</title>')
                        phoneFinalStringAddHeader = (phoneFinalString[:phoneFinalStringIndex + 8] +
                                                     tanmuLink + phoneFinalString[phoneFinalStringIndex + 8:])
                        # pcFinalStringAddHeader = (
                        #             pcFinalString[:pcFinalStringIndex + 8] + tanmuLink + pcFinalString[
                        #                                                                             pcFinalStringIndex + 8:])
                        phoneFinalStringIndex = phoneFinalStringAddHeader.find('</html>')
                        # pcFinalStringIndex = pcFinalStringAddHeader.find('</html>')
                        phoneFinalString = (phoneFinalStringAddHeader[:phoneFinalStringIndex] +
                                                     tanmuContent + phoneFinalStringAddHeader[phoneFinalStringIndex:])
                        # pcFinalString = (
                        #         pcFinalStringAddHeader[:pcFinalStringIndex] + tanmuContent + pcFinalStringAddHeader[
                        #                                                                   pcFinalStringIndex:])

                    path = os.path.join(path, "template")
                    if not os.path.exists(path):
                        os.makedirs(path)
                    filePath = os.path.join(path, str(h5Key) + ".html")
                    phoneFile = open(filePath, "w", encoding="utf-8")
                    phoneFile.write(phoneFinalString.replace("https://img1.maka.im/favicon.ico",
                                                      "https://www.uniecard.com/static/favicon.ico").replace('class="mark"', ''))
                    phoneFile.close()

                    filePath = os.path.join(path, str(h5Key) + "_pc.html")
                    pcFile = open(filePath, "w", encoding="utf-8")
                    pcContent = pcFinalString.replace("https://img1.maka.im/favicon.ico",
                                                      "https://www.uniecard.com/static/favicon.ico").replace(
                        "打开微信", "เปิด Line/Facebook").replace("点击 发现 扫一扫 扫描二维码 可在手机上预览该h5页面",
                                                              "สแกนคิวอาร์โค๊ด เพื่อแสดงผลบนโทรศัพท์").\
                        replace('<img class="pcviewer-infoarea-qrcodearea-img"/>',
                                '<canvas class="pcviewer-infoarea-qrcodearea-img" id="qrcode-canvas"></canvas>').\
                        replace('src="//maka.im/viewer/601736963', 'src="https://www.uniecard.com/viewer/template').replace('class="mark"', '')
                    pcFile.write(pcContent)
                    pcFile.close()
                else:
                    with open(os.path.join(root, "data", "template", "product.json"), 'r', encoding="utf8") as load_f:
                        load_dict = json.load(load_f)
                    for item in load_dict.get("data"):
                        for key in item:
                            if key == 'key' and item[key] == h5Key:
                                data = item
                                break
                    IsPc = pc(phoneUrl, data.get('font'))
                    IsPhone = phone(pcUrl, data.get('font'))
                    phoneIndex = phoneHtml.text.find('<body>')
                    pcIndex = pcHtml.text.find('<body>')
                    path = os.path.join(root, "templates")
                    phoneFinalString = (phoneHtml.text[:phoneIndex + 6] + IsPhone + phoneHtml.text[phoneIndex + 6:])
                    pcFinalString = (pcHtml.text[:pcIndex + 6] + IsPc + pcHtml.text[pcIndex + 6:])
                    if data.get("isTanmu"):
                        phoneFinalStringIndex = phoneFinalString.find('</title>')
                        # pcFinalStringIndex = pcFinalString.find('</title>')
                        phoneFinalStringAddHeader = (phoneFinalString[:phoneFinalStringIndex + 8] +
                                                     tanmuLink + phoneFinalString[phoneFinalStringIndex + 8:])
                        # pcFinalStringAddHeader = (
                        #         pcFinalString[:pcFinalStringIndex + 8] + tanmuLink + pcFinalString[
                        #                                                              pcFinalStringIndex + 8:])
                        phoneFinalStringIndex = phoneFinalStringAddHeader.find('</html>')
                        # pcFinalStringIndex = pcFinalStringAddHeader.find('</html>')
                        phoneFinalString = (phoneFinalStringAddHeader[:phoneFinalStringIndex] +
                                            tanmuContent + phoneFinalStringAddHeader[phoneFinalStringIndex:])
                        # pcFinalString = (
                        #         pcFinalStringAddHeader[:pcFinalStringIndex] + tanmuContent + pcFinalStringAddHeader[
                        #                                                                          pcFinalStringIndex:])
                    path = os.path.join(path, "product")
                    if not os.path.exists(path):
                        os.makedirs(path)
                    filePath = os.path.join(path, str(h5Key) + ".html")
                    phoneFile = open(filePath, "w", encoding="utf-8")
                    phoneFile.write(phoneFinalString.replace("https://img1.maka.im/favicon.ico",
                                                             "https://www.uniecard.com/static/favicon.ico").replace('class="mark"', ''))
                    phoneFile.close()
                    filePath = os.path.join(path, str(h5Key) + "_pc.html")
                    pcFile = open(filePath, "w", encoding="utf-8")
                    pcContent = pcFinalString.replace("https://img1.maka.im/favicon.ico",
                                          "https://www.uniecard.com/static/favicon.ico").replace(
                        "打开微信", "เปิด Line/Facebook").replace("点击 发现 扫一扫 扫描二维码 可在手机上预览该h5页面",
                                                              "สแกนคิวอาร์โค๊ด เพื่อแสดงผลบนโทรศัพท์").\
                        replace('<img class="pcviewer-infoarea-qrcodearea-img"/>',
                                '<canvas class="pcviewer-infoarea-qrcodearea-img" id="qrcode-canvas"></canvas>').\
                        replace('src="//maka.im/viewer/601736963', 'src="https://www.uniecard.com/viewer/product').replace('class="mark"', '')
                    pcFile.write(pcContent)
                    pcFile.close()
                return pretty_result(code.OK, data=[phoneUrl, pcUrl], msg='make h5 successful！')
            except IndexError:
                return pretty_result(code.ERROR,  msg='make h5 failed！')
        else:
            import requests

            pcHeader = {
                'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
            phoneHeader = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'}

            if _type == 'template':
                with open(os.path.join(root, "data", "template", "management.json"), 'r',
                          encoding="utf8") as load_f:
                    load_dict = json.load(load_f)
            else:
                with open(os.path.join(root, "data", "template", "product.json"), 'r',
                          encoding="utf8") as load_f:
                    load_dict = json.load(load_f)
            for item in load_dict.get("data"):
                h5Key = item.get('key')
                pcUrl = 'https://maka.im/pcviewer/601736963/' + str(h5Key)
                phoneUrl = 'https://maka.im/viewer/601736963/' + str(h5Key)
                pcHtml = requests.get(pcUrl, headers=pcHeader)
                phoneHtml = requests.get(phoneUrl, headers=phoneHeader)
                pcHtml.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
                phoneHtml.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
                pcUrl = "https://www.uniecard.com/pcViewer/" + _type + "/" + str(h5Key)
                phoneUrl = "https://www.uniecard.com/viewer/" + _type + "/" + str(h5Key)
                IsPc = pc(phoneUrl, item.get('font'))
                IsPhone = phone(pcUrl, item.get('font'))
                phoneIndex = phoneHtml.text.find('<body>')
                pcIndex = pcHtml.text.find('<body>')
                path = os.path.join(root, "templates")
                data = item
                try:
                    if _type == 'template':
                        phoneFinalString = (phoneHtml.text[:phoneIndex + 6] + IsPhone + templateBtn + phoneHtml.text[
                                                                                                      phoneIndex + 6:])
                        pcFinalString = (pcHtml.text[:pcIndex + 6] + IsPc + pcHtml.text[pcIndex + 6:])
                        if data.get("isTanmu"):
                            phoneFinalStringIndex = phoneFinalString.find('</title>')
                            # pcFinalStringIndex = pcFinalString.find('</title>')
                            phoneFinalStringAddHeader = (phoneFinalString[:phoneFinalStringIndex + 8] +
                                                         tanmuLink + phoneFinalString[phoneFinalStringIndex + 8:])
                            # pcFinalStringAddHeader = (
                            #             pcFinalString[:pcFinalStringIndex + 8] + tanmuLink + pcFinalString[
                            #                                                                             pcFinalStringIndex + 8:])
                            phoneFinalStringIndex = phoneFinalStringAddHeader.find('</html>')
                            # pcFinalStringIndex = pcFinalStringAddHeader.find('</html>')
                            phoneFinalString = (phoneFinalStringAddHeader[:phoneFinalStringIndex] +
                                                tanmuContent + phoneFinalStringAddHeader[phoneFinalStringIndex:])
                            # pcFinalString = (
                            #         pcFinalStringAddHeader[:pcFinalStringIndex] + tanmuContent + pcFinalStringAddHeader[
                            #                                                                   pcFinalStringIndex:])

                        path = os.path.join(path, "template")
                        if not os.path.exists(path):
                            os.makedirs(path)
                        filePath = os.path.join(path, str(h5Key) + ".html")
                        phoneFile = open(filePath, "w", encoding="utf-8")
                        phoneFile.write(phoneFinalString.replace("https://img1.maka.im/favicon.ico",
                                                                 "https://www.uniecard.com/static/favicon.ico").replace(
                            'class="mark"', ''))
                        phoneFile.close()

                        filePath = os.path.join(path, str(h5Key) + "_pc.html")
                        pcFile = open(filePath, "w", encoding="utf-8")
                        pcContent = pcFinalString.replace("https://img1.maka.im/favicon.ico",
                                                          "https://www.uniecard.com/static/favicon.ico").replace(
                            "打开微信", "เปิด Line/Facebook").replace("点击 发现 扫一扫 扫描二维码 可在手机上预览该h5页面",
                                                                  "สแกนคิวอาร์โค๊ด เพื่อแสดงผลบนโทรศัพท์"). \
                            replace('<img class="pcviewer-infoarea-qrcodearea-img"/>',
                                    '<canvas class="pcviewer-infoarea-qrcodearea-img" id="qrcode-canvas"></canvas>'). \
                            replace('src="//maka.im/viewer/601736963',
                                    'src="https://www.uniecard.com/viewer/template').replace('class="mark"', '')
                        pcFile.write(pcContent)
                        pcFile.close()
                    else:
                        phoneFinalString = (phoneHtml.text[:phoneIndex + 6] + IsPhone + phoneHtml.text[phoneIndex + 6:])
                        pcFinalString = (pcHtml.text[:pcIndex + 6] + IsPc + pcHtml.text[pcIndex + 6:])
                        if data.get("isTanmu"):
                            phoneFinalStringIndex = phoneFinalString.find('</title>')
                            # pcFinalStringIndex = pcFinalString.find('</title>')
                            phoneFinalStringAddHeader = (phoneFinalString[:phoneFinalStringIndex + 8] +
                                                         tanmuLink + phoneFinalString[phoneFinalStringIndex + 8:])
                            # pcFinalStringAddHeader = (
                            #         pcFinalString[:pcFinalStringIndex + 8] + tanmuLink + pcFinalString[
                            #                                                              pcFinalStringIndex + 8:])
                            phoneFinalStringIndex = phoneFinalStringAddHeader.find('</html>')
                            # pcFinalStringIndex = pcFinalStringAddHeader.find('</html>')
                            phoneFinalString = (phoneFinalStringAddHeader[:phoneFinalStringIndex] +
                                                tanmuContent + phoneFinalStringAddHeader[phoneFinalStringIndex:])
                            # pcFinalString = (
                            #         pcFinalStringAddHeader[:pcFinalStringIndex] + tanmuContent + pcFinalStringAddHeader[
                            #                                                                          pcFinalStringIndex:])
                        path = os.path.join(path, "product")
                        if not os.path.exists(path):
                            os.makedirs(path)
                        filePath = os.path.join(path, str(h5Key) + ".html")
                        phoneFile = open(filePath, "w", encoding="utf-8")
                        phoneFile.write(phoneFinalString.replace("https://img1.maka.im/favicon.ico",
                                                                 "https://www.uniecard.com/static/favicon.ico").replace(
                            'class="mark"', ''))
                        phoneFile.close()
                        filePath = os.path.join(path, str(h5Key) + "_pc.html")
                        pcFile = open(filePath, "w", encoding="utf-8")
                        pcContent = pcFinalString.replace("https://img1.maka.im/favicon.ico",
                                                          "https://www.uniecard.com/static/favicon.ico").replace(
                            "打开微信", "เปิด Line/Facebook").replace("点击 发现 扫一扫 扫描二维码 可在手机上预览该h5页面",
                                                                  "สแกนคิวอาร์โค๊ด เพื่อแสดงผลบนโทรศัพท์"). \
                            replace('<img class="pcviewer-infoarea-qrcodearea-img"/>',
                                    '<canvas class="pcviewer-infoarea-qrcodearea-img" id="qrcode-canvas"></canvas>'). \
                            replace('src="//maka.im/viewer/601736963',
                                    'src="https://www.uniecard.com/viewer/product').replace('class="mark"', '')
                        pcFile.write(pcContent)
                        pcFile.close()
                except IndexError:
                    return pretty_result(code.ERROR, msg='make h5 all failed！')
            return pretty_result(code.OK, data="", msg='make h5 all successful！')


class WebsiteResource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        try:
            return make_response(render_template('index.html'), 200, headers)
        except IndexError:
            abort(404)


class WebsiteV2Resource(Resource):
    """
    test list资源类
    """
    # decorators = [limiter.exempt]
    # decorators = [limiter.limit("1/day")]

    def __init__(self):
        self.parser = RequestParser()

    # @swag_from('../../docs/swagger/admin/test/test_get.yml', methods=['GET'])
    def get(self):
        """
        Test Method

        swagger_from_file: ../../docs/swagger/test_get.yml

        """
        try:
            return make_response(render_template('index_v2.html'), 200, headers)
        except IndexError:
            abort(404)