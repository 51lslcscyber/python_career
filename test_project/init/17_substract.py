# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/6/27 23:47
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 以下方法可在一行中调用多个函数。


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 4, 5
print((subtract if a > b else add)(a, b))  # 9
if __name__ == "__main__":
    pass