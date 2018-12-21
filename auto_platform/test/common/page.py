# -*- coding: utf-8 -*-
# @Time     : 2018/10/31 16:57
# @Author   : Philly
# @Site     : 
# @File     : page.py
# @Software : PyCharm Community Edition
from auto_platform.test.common.browser import Browser


class Page(Browser):
    # 更多的封装请自己动手^-^
    def __init__(self, page=None, browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)