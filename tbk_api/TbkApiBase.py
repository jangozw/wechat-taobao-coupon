#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import hashlib
import urllib.parse
import requests


class TbkApiBase(object):
    # 接口网关
    __api_url = 'http://gw.api.taobao.com/router/rest'
    #  调用api的key (这些都在淘宝联盟里操作申请)
    __app_key = '26030486'
    # 调用api的secret
    __app_secret = '8c0ceba84c3a340bc95caf3003b17f22'
    # 淘宝联盟id
    tbk_uid = '44530088'
    # 推广位ID (在淘宝联盟里推广位建)
    tbk_adzoneid = '108546050417'

    def __init__(self):
        pass

    def pub_params(self):
        param = {
            'app_key': self.__app_key,
            'v': '2.0',
            'sign_method': 'md5',
            'format': 'json',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            # 'method': 'taobao.tbk.dg.material.optional',
        }
        return param

    # 淘宝接口请求
    def request(self, method, params):
        params_req = self.pub_params()
        params['method'] = method
        for k, v in params.items():
            params_req[k] = v
        print("淘客接口 "+method+" 请求参数：", params_req)
        # 合成url 并返以json形式返回数据
        sign = self.createSign(params_req)
        strParam = self.createStrParam(params_req)
        strParam += 'sign=' + sign
        url = self.__api_url+'?' + strParam
        res = requests.get(url)
        print("淘客接口 "+method+" 返回结果：", res.text)
        d = self.parse_api_res(method, res.json())
        return d

    #排序
    def ksort(self, d):
        return [(k, d[k]) for k in sorted(d.keys())]

    # md5加密
    def md5(self, s, raw_output=False):
        res = hashlib.md5(s.encode())
        if raw_output:
            return res.digest()
        return res.hexdigest()

    # 制作签名
    def createSign(self, params):
        sign = self.__app_secret
        params = self.ksort(params)
        params = dict(params)
        # print(paramArr)
        for k, v in params.items():
            if k != '' and v != '':
                sign += k + v
        sign += self.__app_secret
        # print(sign)
        sign = self.md5(sign).upper()
        return sign

    # 组合参数
    def createStrParam(self, paramArr):
        strParam = ''
        for k, v in paramArr.items():
            if k != '' and v != '':
                strParam += k + '=' + urllib.parse.quote_plus(v) + '&'  # 进行编码操作
        return strParam

    # 解析api返回结果
    def parse_api_res(self, method, json):
        key = method.replace('taobao.', '')
        key = key.replace('.', '_') + '_response'
        if key in json:
            return json[key]
        else:
            err_key = 'error_response'
            if err_key in json:
                print("Api结果返回失败,error="+json[err_key]['msg'] + ' ' + json[err_key]['sub_msg'])
            return
