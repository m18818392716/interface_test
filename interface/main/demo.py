#-*- coding:utf-8 -*-
# @Time    : 2019/3/29 下午3:03
# @Author  : Susanna Chen
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

import requests,json

lists = ['python', 'php', 'Java']

for i in lists:
    url = 'http://www.baidu.com/s?wd=%s' % (str(i))
    r = requests.get(url)
    print(r.url)


params = {'wd': 'python'}
print(type(params))
lists1 = [1, 2, 3]

for i in lists1:
    url1 = 'https://proj.gtomato.com.cn/mobile/v1/customer/%s/overview' % (str(i))
    r = requests.get(url1)
    print(r.url)


# 链接地址：https://www.cnblogs.com/peak911/p/9804404.html
# loads()：将json数据转化成dict数据
# dumps()：将dict数据转化成json数据

# load()：读取json文件数据，转成dict数据
# dump()：将dict数据转化成json数据后写入json文件

data = {'key1': '1', 'key2': '2'}
print('data 的类型是：%s' % type(data))
dataStr = json.dumps(data)
print('json.dumps(data) 操作后的类型是：%s' % type(dataStr))


dataDict = json.loads(dataStr)
print('json.loads(data1) 操作后的类型是：%s' % type(dataDict))


#读取json文件,转成dict数据
def read_data():
    with open('../dataconfig/header.json', 'rb') as fp:
        data = json.load(fp)
        return data

jsonDict = read_data()
print('jsonDict 的类型是：%s' % type(jsonDict))
print(jsonDict)



# 将dict数据转化成json数据后写入json文件
def write_data(dictData):
    with open('../dataconfig/demo.json', 'wb') as fp:
        fp.write(json.dumps(dict(dictData)).encode('utf-8'))
        fp.close()  # 关闭文件

jsonStr = write_data(jsonDict)
print('jsonStr 的类型是：%s' % type(jsonStr))
print(jsonStr)