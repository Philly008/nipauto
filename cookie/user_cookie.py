# -*- coding: utf-8 -*-
# @Time     : 2018/10/29 15:38
# @Author   : Philly
# @Site     : 
# @File     : user_cookie.py
# @Software : PyCharm Community Edition
from selenium import webdriver
import time, yaml, os

url = 'http://readfree.me/'
chromedriver_path = (r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.maximize_window()
driver.delete_all_cookies()
time.sleep(3)
driver.get(url)

fileNamePath = os.path.split(os.path.realpath(__file__))[0]
yamlPath = os.path.join(fileNamePath, 'config.yaml')
f = open(yamlPath, 'r', encoding='utf-8')
cont = f.read()
conf = yaml.load(cont)
cookie1 = conf.get("cookie1")
driver.add_cookie(cookie1)
print("cookies: " + str(driver.get_cookies()))
time.sleep(3)
driver.get(url)
time.sleep(2)
driver.refresh()
time.sleep(3)
driver.quit()
