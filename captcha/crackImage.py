# -*- coding: utf-8 -*-
# @Time       : 2018/11/20 13:30
# @Author     : Philly
# @File       : crackImage.py
# @Description: 实时获取并解析图片验证码进行登录系统
import tesserocr
from PIL import Image
from urllib import request
from selenium import webdriver
from time import sleep
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import os
import re




# 把验证码另存为图片
def image_save_as():
    image = driver.find_element_by_id("valiCode")
    actions = ActionChains(driver)
    actions.context_click(image)
    actions.perform()
    pyautogui.typewrite(['down', 'down', 'enter', 'enter']) # 右键找到图片另存为
    sleep(2)
    pyautogui.typewrite(['enter'])
    sleep(2)

def get_newest_image(image_path):

    lists = os.listdir(image_path)
    lists.sort(key=lambda fn:os.path.getmtime(image_path + "\\" + fn))  # 按时间排序
    image_new = os.path.join(image_path, lists[-1])

    return image_new


"""
driver.save_screenshot("all.png")
print(image.location, image.size)
left = image.location['x']
top = image.location['y']
right = image.location['x'] + image.size['width']
bottom = image.location['y'] + image.size['height']

im = Image.open('all.png')
im = im.crop((left, top, right, bottom))
im.save('code9.png')

imageUrl = url2 + "/GetValidateCode"
request.urlretrieve(imageUrl, "code8.jpg")  # 把图片保存到本地code8.jpg

"""
# 转换验证码图片为文字
def image_to_txt(image_new):
    image = Image.open(image_new)
    image = image.convert('L')
    threshold = 80  # 设置阈值
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table, '1')
    result = tesserocr.image_to_text(image)
    f = open('result.txt', 'w')
    f.write(result)
    f.close()
    # 去掉中间空格
    result_e = ''.join(result.split())
    # 只取数字
    result_w = re.findall('\d+', result_e)[0]

    return result_w

def login(result_w):
    driver.find_element_by_id("LoginAccount").send_keys("zbsqy")
    sleep(1)
    driver.find_element_by_id("Password").send_keys("admin")
    sleep(1)
    driver.find_element_by_id("verifyCode").send_keys(result_w)
    sleep(1)
    driver.find_element_by_id("btnLogin").click()
    sleep(3)


if __name__ == "__main__":



    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.14.38:88/User/Login")
    sleep(2)

    image_path = r"C:\Users\hasee\Downloads"    # 验证码另存为的路径

    image_save_as()
    image_new = get_newest_image(image_path)
    result_w = image_to_txt(image_new)
    login(result_w)