# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/6 15:52
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 以下方法返回列表中出现的最常见元素。

def most_frequent(list):
    return max(set(list), key=list.count)


list = [1, 2, 1, 2, 3, 2, 1, 4, 2]
most_frequent(list)
if __name__ == "__main__":
    pass
