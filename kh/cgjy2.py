# -*- coding: utf-8 -*-
# @Time       : 2018/11/22 10:12
# @Author     : Philly
# @File       : cgjy2.py
# @Description: 

from pywinauto.application import Application
from pywinauto import mouse, keyboard
from time import sleep


# Run a target application
app = Application(backend="uia").start(r"E:\云康\康华\Release集群\DaanWinApp.exe") # 启动程序
sleep(2)
mouse.click(button="left", coords=(963, 554))   # 点击确定缺少配置文件提示
sleep(1)
# 双击账号并取消文本
mouse.double_click(button="left", coords=(925,567))
keyboard.SendKeys('{BACKSPACE}')    # 键盘 BACKSPACE
keyboard.SendKeys('admingltest')    # 输入账号
sleep(1)
keyboard.SendKeys('{TAB}')    # TAB
keyboard.SendKeys('{BACKSPACE}')    # 键盘 BACKSPACE
keyboard.SendKeys('123abc')    # 输入密码
sleep(1)
2

mouse.click(button="left", coords=(979, 684))   # 点击登录
sleep(3)
app = app.connect(title_re="康华检验平台", class_name="WindowsForms10.Window.8.app.0.2eed1ca_r9_ad1")     # 连接到现运行程序
# print(app["康华检验平台"].print_control_identifiers())  # 显示窗口的子窗口、控件等
# print(app.top_window().print_control_identifiers())
# print(app["康华检验平台"]['Dock Top'].print_control_identifiers())

mouse.click(button="left", coords=(193, 41))    # 点击检验管理
sleep(1)
mouse.click(button="left", coords=(212, 74))    # 点击常规检验
sleep(3)
mouse.click(button="left", coords=(588,253))    # 点击仪器文本框
keyboard.SendKeys('{BACKSPACE}')    # 键盘 BACKSPACE
keyboard.SendKeys('E601发光仪')    # 输入仪器名称
sleep(1)
keyboard.SendKeys('{ENTER}')    # 回车


for i in range(89,96):
    tmh = '20181122' + str(i) + '00'
    keyboard.SendKeys('{F1}')   # F1新增
    mouse.click(button="left", coords=(572,318))    # 点击条码号文本框
    keyboard.SendKeys(tmh)   # 输入条码号

    mouse.click(button="left", coords=(605,417))    # 姓名
    keyboard.SendKeys('xingming')
    mouse.click(button='left', coords=(590,451))    # 性别
    keyboard.SendKeys('男')
    sleep(0.5)
    keyboard.SendKeys('{ENTER}')
    sleep(0.5)
    mouse.click(button='left', coords=(587,481))    # 年龄
    keyboard.SendKeys('33')

    mouse.click(button='left', coords=(906,225))    # 项目
    keyboard.SendKeys('甲状旁腺素')
    sleep(0.5)
    keyboard.SendKeys('{ENTER}')
    sleep(1)
    mouse.click(button='left', coords=(1265,319))   # 项目结果
    keyboard.SendKeys('2')
    sleep(0.5)
    keyboard.SendKeys('{ENTER}')
    sleep(0.5)
    keyboard.SendKeys('{F2}')   # 保存
    sleep(2)



