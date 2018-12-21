# -*- coding: utf-8 -*-
# @Time     : 2018/10/31 17:03
# @Author   : Philly
# @Site     : 
# @File     : baidu_result_page.py
# @Software : PyCharm Community Edition
from selenium.webdriver.common.by import By
from auto_platform.test.page.baidu_main_page import BaiDuMainPage


class BaiDuResultPage(BaiDuMainPage):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)