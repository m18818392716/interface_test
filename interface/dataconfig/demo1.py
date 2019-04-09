#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 上午10:31
# @Author  : Susanna Chen
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm
import re
# print(0 == 0.00)
# print(0 == 0.0)


def is_2dp_format(number):
    # regex = re.compile(r"^(-?\d+)(\.\d*)?$")
    regex = re.compile(r"^[0-9]+(.[0-9]{2})+$")

    if re.match(regex, number):
        print('%s 是保留两位的小数' % number)
        return True

    else:
        print('%s 不是保留两位的小数' % number)
        return False

def is_iso3_format(str):
    regex = re.compile('^[A-Z]{3}$')

    if re.match(regex, str):
        print('%s 是ISO3 code的格式' % str)
        return True

    else:
        print('%s 不是ISO3 code的格式' % str)
        return False

def is_date_format(str):
    regex = re.compile('^([1-9]|[12][0-9]|3[01])[ ](January|February|March|April|May|June|July|August|September|October|November|December)[ ](\d+)$')

    if re.match(regex, str):
        print('%s 是DD Mmm YYYY的格式' % str)
        return True

    else:
        print('%s 不是DD Mmm YYYY的格式' % str)
        return False
# 一、判断一个数是否为小数
#
# 1、有且仅有一个小数点
#
# 2、小数点的左边可能为正数或负数
#
# 3、小数点的右边为正数

def is_float(str):
    if str.count('.') == 1: #小数有且仅有一个小数点
        left = str.split('.')[0]  #小数点左边（整数位，可为正或负）
        right = str.split('.')[1]  #小数点右边（小数位，一定为正）
        lright = '' #取整数位的绝对值（排除掉负号）
        if str.count('-') == 1 and str[0] == '-': #如果整数位为负，则第一个元素一定是负号
            lright = left.split('-')[1]
        elif str.count('-') == 0:
            lright = left
        else:
            print('%s 不是小数'%str)
        if right.isdigit() and lright.isdigit(): #判断整数位的绝对值和小数位是否全部为数字
            print('%s 是小数'%str)
        else:
            print('%s 不是小数'%str)
    else:
        print('%s 不是小数'%str)


# 30.112 是小数
# -300.123 是小数
# -.5 不是小数
# 2-1 不是小数
# --11..22 不是小数
# 5. 不是小数
# 0 不是小数
# abc.efg 不是小数
is_float('30.112')
is_float('-300.123')
is_float('-.5')
is_float('2-1')
is_float('--11..22')
is_float('5.')
is_float('0')
is_float('abc.efg')



is_2dp_format('0.00')
is_2dp_format('0.0')
is_2dp_format('0')


is_iso3_format('abc')
is_iso3_format('Abc')
is_iso3_format('ABC')

is_date_format('9 January 2019')
is_date_format('21 January 2019')
is_date_format('33 January 2019')
is_date_format('1 January 20190')
is_date_format('9 Jan 2019')

