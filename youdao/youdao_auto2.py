# -*- coding: utf-8 -*-
# @Time       : 2018/11/19 16:30
# @Author     : Philly
# @File       : youdao_auto2.py
# @Description: 自动签到有道云笔记
from time import sleep
from pywinauto import application, mouse
import os

os.getcwd()     # 显示当前工作目录
os.chdir("D:")  # 切换到D盘
os.chdir("D:\\Program Files\\YoudaoNote")   # 切换到有道应用启动的路径下
cmdline = os.getcwd() + '\YoudaoNote.exe'
# 启动有道云笔记
# app = application.Application(backend="uia").start(cmdline) # 默认的backend win32
app = application.Application().start(cmdline) # 默认的backend win32
sleep(8)
mouse.click(button='left', coords=(50, 71))
sleep(3)
mouse.click(button='left', coords=(1180, 261))
sleep(2)
mouse.click(button='left', coords=(1445, 206))
sleep(1)
mouse.click(button='left', coords=(1892, 26))
sleep(1)





