# -*- coding: utf-8 -*-
# @Time     : 2018/11/15 16:43
# @Author   : Philly
# @Site     : 
# @File     : parse_captcha.py
# @Software : PyCharm Community Edition
from lxml.html import fromstring
import requests
from io import BytesIO
from PIL import Image
import base64
import pytesseract

def parse_form(html):
    tree = fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):    # pip install cssselect
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data

def get_captcha_img(html):
    tree = fromstring(html)
    img_data = tree.cssselect('div img#verifyCode').get('src')
    # img_data = img_data.partition(',')[-1]
    binary_img_data = base64.b64decode(img_data)
    img = Image.open(BytesIO(binary_img_data))
    return img

if __name__ == '__main__':
    html = requests.get('http://192.168.14.38:88/User/Login')
    form = parse_form(html.content)
    print(form)

    img = get_captcha_img(html.content)
    tessdata_dir_config = '--tessdata-dir "D:\\testsoft\\Tesseract-OCR\\tessdata"'
    pytesseract.image_to_string(img, tessdata_dir_config)