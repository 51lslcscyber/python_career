# -*- coding: utf-8 -*-

# @Time:2022/2/13
#@version:
# Created by: Python3.9.6
#@author:鹄思鹄想bit森
# WARNING: run again.  Do not edit this file unless you know what you are doing.
'''
# 1.使用python将图片转化为base64字符串
'''
import base64
f=open('G:\捕获.PNG','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(ls_f)
'''
base64字符串转化为图片
'''
# import base64
# bs=''
# imgdata=base64.b64decode(bs)
# file=open('2.jpg','wb')
# file.write(imgdata)
# file.close()