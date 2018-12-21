# -*- coding: utf-8 -*-
# @Time     : 2018/11/1 11:04
# @Author   : Philly
# @Site     : 
# @File     : test_baidu_http.py
# @Software : PyCharm Community Edition
import unittest
from auto_platform.utils.config import Config, REPORT_PATH
from auto_platform.utils.client import HTTPClient
from auto_platform.utils.log import logger
from auto_platform.utils.HTMLTestRunner import HTMLTestRunner
from auto_platform.utils.assertion import asserHTTPCode

## socket 库测TCP接口，suds库测SOAP接口
class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')
    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        asserHTTPCode(res, [400])
        self.assertIn('百度一下，你就知道', res.text)

if __name__ == 'test_baidu_http':
    report = REPORT_PATH + '\\report_http.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试框架', description='接口测试报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))

