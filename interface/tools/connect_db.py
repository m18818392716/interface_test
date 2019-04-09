#-*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:51
# @Author  : Susanna Chen
# @Site    : 
# @File    : connect_db.py
# @Software: PyCharm

import MySQLdb.cursors
import json

class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456789',
            db='testcase',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
            )
        self.cur = self.conn.cursor()

    #查询一条数据
    def search_one(self,sql):
        print(sql)
        print(type(sql))
        self.cur.execute(sql.encode('utf-8'))
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from testcase.testapi_sign_event where name='小米5发布会'")
    print(res)