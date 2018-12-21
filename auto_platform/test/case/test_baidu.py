# -*- coding: utf-8 -*-
# @Time     : 2018/10/30 15:42
# @Author   : Philly
# @Site     : 
# @File     : test_baidu.py
# @Software : PyCharm Community Edition
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://www.baidu.com"
print('当前py文件的路径是：' + __file__)
# py文件的上级路径 \..
base_path = os.path.dirname(os.path.abspath(__file__ + '\..\..'))
print('基础路径是：'+ base_path)
driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
# 查找相对路径 // 下 div 节点的class 属性包含 result 内容的元素
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
driver.quit()





