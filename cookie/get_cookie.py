# -*- coding: utf-8 -*-
# @Time     : 2018/10/29 15:17
# @Author   : Philly
# @Site     : 
# @File     : get_cookie.py
# @Software : PyCharm Community Edition
import yaml, time, os
from selenium import webdriver

url = 'http://readfree.me/'
chromedriver_path = (r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get(url)
driver.maximize_window()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="navbar"]/div/div/ul/li[1]/a').click()
time.sleep(2)
cookie_before = driver.get_cookies()
print('登录前的 cookies为：' + str(cookie_before))
time.sleep(1)

driver.find_element_by_id(u'id_email').clear()
driver.find_element_by_id(u'id_email').send_keys('liuup66@163.com') # 邮箱
time.sleep(1)
driver.find_element_by_id(u'id_password').clear()
driver.find_element_by_id(u'id_password').send_keys('Liushui68')    # 密码
print('请手动输入验证码：')
security_code = input()
time.sleep(3)
driver.find_element_by_id('id_captcha_1').send_keys(security_code)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="id_signin_form"]/div[1]/button').click()
time.sleep(3)

cookie_after = driver.get_cookies()
print('得到的cookies为：' + str(cookie_after))
len1 = len(cookie_after)
cookie1 = cookie_after[0]   # 比对登录前后的cookie，获取账号密码的cookie
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
yamlPath = os.path.join(fileNamePath, 'config.yaml')
fw = open(yamlPath, 'w', encoding='utf-8')
data = {"cookie1":cookie1}
yaml.dump(data, fw)

driver.quit()



