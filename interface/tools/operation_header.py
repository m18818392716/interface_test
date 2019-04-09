#-*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:52
# @Author  : Susanna Chen
# @Site    : 
# @File    : operation_header.py
# @Software: PyCharm

import requests
import json
from interface.tools.operation_json import OperetionJson


class OperationHeader:

    # def __init__(self, response):
    #     self.response = json.loads(response)


    # def get_response_url(self):
    #     '''
    #     获取登录返回的token的url
    #     '''
    #     url = self.response['data']['url'][0]
    #     return url

    def get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        # url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        url = "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperetionJson()
        op_json.write_data(cookie)


    def get_header(self):
        # header = self.response.headers
        url = 'http://localhost:8080/mobile/v1/customer/userprofile'
        headers = {"AMSESSION":"ukdata5", "Region":"uk", "Content-Type": "application/json;charset=UTF-8"}
        header = requests.get(url=url, headers=headers, verify=False).headers
        return header

    def write_header(self):
        # header = requests.utils.parse_dict_header()
        op_json = OperetionJson()
        op_json.write_header(self.get_header())


if __name__ == '__main__':
    url = "http://www.jd.com/passport/user/login"
    data = {
        "username": "18513199586",
        "password": "111111",
        "verify": "",
        "referer": "https://www.jd.com"
    }
    res = json.dumps(requests.post(url, data).json())
    op_header = OperationHeader(res)
    op_header.write_cookie()