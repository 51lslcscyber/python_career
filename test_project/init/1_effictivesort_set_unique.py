# -*- coding: utf-8 -*-

# @Time:2022/0/
#@version:
# Created by: Python3.9.6
#@author:鹄思鹄想bit森
# WARNING: run again.  Do not edit this file unless you know what you are doing.
# 检查重复元素
def all_unique(lst):
    return len(lst)==len(set(lst))
x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6, ]
y = [1, 2, 3, 4, 5]
all_unique(x)#false
all_unique(y)#true
print(all_unique(x))
print(all_unique(y))