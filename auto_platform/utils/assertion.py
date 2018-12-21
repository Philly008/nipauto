# -*- coding: utf-8 -*-
# @Time     : 2018/11/1 15:10
# @Author   : Philly
# @Site     : 
# @File     : assertion.py
# @Software : PyCharm Community Edition
"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
"""
def asserHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应Code不在列表中！')    # 抛出AssertionError, unittest会自动判断用例为Failure