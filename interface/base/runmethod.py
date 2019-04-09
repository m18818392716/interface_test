#-*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:49
# @Author  : Susanna Chen
# @Site    : 
# @File    : runmethod.py
# @Software: PyCharm

import requests

# 解决提示'InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings'
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import json
class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header !=None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        # return res.json()

        if res.content:
            return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header !=None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        # return res.json()
        if res.content:
            return res.json()

    def run_main(self,method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)

        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        # return res



    def post_request(self, url, data, header=None):
        res = None
        if header !=None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)

        if res.content:
            # print('请求url：%s' % res.url)
            return res

    def get_request(self, url, data=None, header=None):
        res = None
        if header !=None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)

        if res.content:
            # print('请求url：%s' % res.url)
            return res

    def run_request(self,method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_request(url, data, header)
        else:
            res = self.get_request(url, data, header)

        return res