#-*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:52
# @Author  : Susanna Chen
# @Site    : 
# @File    : operation_json.py
# @Software: PyCharm


#coding:utf-8
import json

class OperetionJson:

    def __init__(self,file_path=None):
        if file_path  == None:
            self.file_path = '../dataconfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path, 'rb') as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        print(type(self.data))
        if id == '':
            return None
        else:
            return self.data[id]

    #写json
    def write_data(self,data):
        with open('../dataconfig/cookie.json', 'wb') as fp:
            fp.write(json.dumps(dict(data)).encode('utf-8'))
            # json.dump(data,fp)
            fp.close()  # 关闭文件

    # 写json
    def write_header(self, data):
        with open('../dataconfig/header.json', 'wb') as fp:
            fp.write(json.dumps(dict(data)).encode('utf-8'))
            # fp.write(json.dumps(list(data), ensure_ascii=False))
            # json.dump(data, fp)
            fp.close()  # 关闭文件



if __name__ == '__main__':
    opjson = OperetionJson()
    print(opjson.get_data('shop'))