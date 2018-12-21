# -*- coding: utf-8 -*-
# @Time     : 2018/10/31 17:07
# @Author   : Philly
# @Site     : 
# @File     : test_baidu_2.py
# @Software : PyCharm Community Edition
import os
import time
import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from auto_platform.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from auto_platform.utils.log import logger
from auto_platform.utils.file_reader import ExcelReader
from auto_platform.utils.HTMLTestRunner import HTMLTestRunner
from auto_platform.utils.mail import Email
from auto_platform.test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == 'test_baidu_2':      # 如果为 __main__ 时一直无法生成报告。所以改为文件名即可。
    warnings.simplefilter("ignore", ResourceWarning)
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架', description='html测试报告')
        runner.run(TestBaiDu('test_search'))

    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='liushuiliu@yunkanghealth.com',
              server='smtp.yunkanghealth.com',
              sender='liushuiliu@yunkanghealth.com',
              password='liushui68',
              path=report
              )
    e.send()

