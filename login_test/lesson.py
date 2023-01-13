#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/1/13 15:24
# @Author   : wqh
# @Email    : 867075698@qq.com
# @File     : lesson.py
# @Software : PyCharm


import requests


def test_login():
    url = 'http://www.baidu.com'
    data = {"datas": "java"}
    res = requests.get(url, data)
    return res
