# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/6/18 12:43
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 该方法只保留第一个迭代器中的值，从而发现两个迭代器之间的差异。
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)
    difference([1, 2, 3], [1, 2, 4])  # [3]


if __name__ == "__main__":
    pass
