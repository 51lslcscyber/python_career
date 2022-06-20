# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/6/18 12:35
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
            return ret


def deep_flatten(lst):
    result = []
    result.extend(
        spread(
            list(map(lambda x: deep_flatten(x) if type(x) == list else x,
                     lst))))
    return result
    deep_flatten([1, [2], [[3], 4], 5])  # [1,2,3,4,5]
