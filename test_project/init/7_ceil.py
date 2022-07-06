# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/6/16 23:53
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 以下方法使用 range() 将列表分块为指定大小的较小列表。

from math import ceil


def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))


chunk([1, 2, 3, 4, 5], 2)  # [[1,2],[3,4],5]
if __name__ == "__main__":
    pass