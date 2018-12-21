# -*- coding: utf-8 -*-
# @Time     : 2018/10/30 17:23
# @Author   : Philly
# @Site     : 
# @File     : test_baidu_1.py
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

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == 'test_baidu_1':      # 如果为 __main__ 时一直无法生成报告。所以改为文件名即可。
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
              password='XXX',
              path=report
              )
    e.send()

