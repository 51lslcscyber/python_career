# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/6 20:07
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 以下代码段将展示如何编写一个不使用 if-else 条件的简单计算器。
import operator

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25))  # 25
if __name__ == "__main__":
    pass
