#-*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:51
# @Author  : Susanna Chen
# @Site    : 
# @File    : common_util.py
# @Software: PyCharm

import re
import json
import operator
from interface.tools.compare_json import compare_json

class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否再另外一个字符串中
        str_one:查找的字符串
        str_two：被查找的字符串
        '''
        flag = None

        # if isinstance(str_one, str):
        #     str_one = str_one.encode('unicode-escape').decode('string_escape')
        # return operator.eq(str_one,str_two)

        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag


    def is_equal_dict(self,dict_one,dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)

        print('expect dict_one:')
        print(dict_one)
        print(type(dict_one))
        print('actual dict_two:')
        print(dict_two)
        print(type(dict_two))
        # print(dict_one == dict_two)
        # return operator.eq(dict_one,dict_two)
        return compare_json(json.dumps(dict_one), json.dumps(dict_two))

    def is_2dp_format(self,number):

        regex = re.compile(r"^[0-9]+(.[0-9]{2})+$")

        if re.match(regex, number):
            return True

        else:
            return False