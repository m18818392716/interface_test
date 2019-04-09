#-*- coding:utf-8 -*-
# @Time    : 2019/4/1 下午12:31
# @Author  : Susanna Chen
# @Site    : 
# @File    : compare_json.py
# @Software: PyCharm

# 对json进行比较（忽略列表中字典的顺序）
import json

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

def compare_json(a, b):
    aa = json.loads(a)
    bb = json.loads(b)

    len_a = len(aa)
    len_b = len(bb)
    if len_a != len_b:
        return False
    else:
        for key in aa:
            # if not bb.has_key(key):
            if key not in bb:
                return False
            else:
                # if sorted(aa[key]) != sorted(bb[key]):
                if ordered(aa) != ordered(bb):
                    return False
    return True


if __name__ == "__main__":
    a = '{"ROAD": [{"id": 123}, {"name": "no1"}]}'
    b = '{"ROAD": [{"name": "no1"}, {"id": 123}]}'

    c = '{"code": "1001", "message": "error!", "data": {"base": {"code": "GBP", "rate": 1.0}}}'
    d = '{"code": "1001", "data": {"base": {"code": "GBP", "rate": 1.00}}, "message": "error!"}'
    print(compare_json(c, d))