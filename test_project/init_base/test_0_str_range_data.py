# -*- coding: utf-8 -*-

# @Time:2021/10/06
#@version:
# Created by: Python3.9.6
#@author:鹄思鹄想bit森
# WARNING: 
# run again.  Do not edit this file unless you know what you are doing.
#一些自己想到的题，结合性的知识
for i in range(10):
    print(i)
print('1')
#continue中断，遍历范围取前不取后
for i in range(6):
    if i%4==0:continue
    else:
        print(i,end=",")