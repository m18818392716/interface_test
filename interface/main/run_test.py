#-*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:50
# @Author  : Susanna Chen
# @Site    : 
# @File    : run_test.py
# @Software: PyCharm

import sys
sys.path.append("/Users/gzuser/PycharmProjects/DemoTest1/interface")
from interface.base.runmethod import RunMethod
from interface.operation_data.get_data import GetData
from interface.tools.common_util import CommonUtil
from interface.operation_data.dependent_data import DependdentData
from interface.tools.send_email import SendEmail
from interface.tools.operation_header import OperationHeader
from interface.tools.operation_json import OperetionJson
import requests
import json
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mai = SendEmail()
        self.headers = {"AMSESSION":"ukdata5", "Region":"uk", "Content-Type": "application/json;charset=UTF-8"}

    #程序执行的
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        #10  0,1,2,3
        rows_count = self.data.get_case_lines()
        print('rows_count: %d' % rows_count)
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                # expect = self.data.get_expcet_data_for_mysql(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    #获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    print('依赖关键字：%s' % depend_key)
                    print(depend_response_data)
                    print('依赖值类型：%s' % type(depend_response_data))
                    print('请求数据：%s' % request_data)
                    print('请求数据类型：%s' % type(request_data))

                    if request_data != None:
                        request_data1 = json.loads(request_data)
                        request_data1[depend_key] = depend_response_data
                        request_data = json.dumps(request_data1)
                        print(request_data)
                    else:
                        if method == 'Post':
                            request_data1 = {}
                            request_data1[depend_key] = depend_response_data
                            request_data = json.dumps(request_data1)
                            print(request_data)
                        else:
                            request_data1 = {}
                            request_data1[depend_key] = depend_response_data
                            request_data = request_data1
                            print(request_data)

                if header == 'write':
                    res = self.run_method.run_main(method, url, request_data, self.headers)
                    response = self.run_method.run_request(method, url, request_data, self.headers)
                    print('请求url：%s' % response.url)
                    print('请求参数：%s' % request_data)
                    print('请求参数类型：%s' % type(request_data))
                    print('返回状态码：%s' % response.status_code)
                    # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
                    print(res)
                    # op_header = OperationHeader(res)
                    op_header = OperationHeader()
                    # op_header.write_cookie()
                    op_header.write_header()

                elif header == 'yes':
                    op_json = OperetionJson('../dataconfig/cookie.json')
                    header_json = OperetionJson('../dataconfig/header.json')

                    amsession = header_json.get_data('AMSESSION')
                    token = header_json.get_data('LtpaToken2')
                    content = header_json.get_data('Content-Type')
                    # cookie = op_json.get_data('apsid')
                    # cookies = {
                    #     'apsid':cookie
                    # }
                    headers = {
                        'AMSESSION':amsession,
                        'LtpaToken2':token,
                        'Content-Type':content
                    }

                    # res = self.run_method.run_main(method,url,request_data,cookies)
                    res = self.run_method.run_main(method, url, request_data, headers)

                    response = self.run_method.run_request(method, url, request_data, headers)
                    print('请求url：%s' % response.url)

                    print('请求参数：%s' % request_data)
                    print('请求参数类型：%s' % type(request_data))
                    print('返回状态码：%s' % response.status_code)
                    # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
                    print(res)
                else:
                    res = self.run_method.run_main(method, url, request_data)

                    response = self.run_method.run_request(method, url, request_data)
                    print('请求url：%s' % response.url)

                    print('请求参数：%s' % request_data)
                    print('请求参数类型：%s' % type(request_data))
                    print('返回状态码：%s' % response.status_code)
                    # print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
                    print(res)

                if self.com_util.is_equal_dict(expect,res) == True:
                    # self.data.write_result(i,'pass')
                    pass_count.append(i)
                    print('expect result type is: %s' % type(expect))
                    print('actual result type is: %s' % type(res))
                    print('pass test.......')
                else:
                    # self.data.write_result(i,res)
                    fail_count.append(i)
                    print('expect result type is: %s' % type(expect))
                    print('actual result type is: %s' % type(res))
                    print('fail test.......')
        # self.send_mai.send_main(pass_count,fail_count)
        print(pass_count)
        print(fail_count)

    #将执行判断封装
    #def get_cookie_run(self,header):


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()