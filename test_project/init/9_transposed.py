# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/6/16 23:52
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 以下代码段可以用来转换一个二维数组。

array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed)  # [('a', 'c', 'e'), ('b', 'd', 'f')]
if __name__ == "__main__":
    pass