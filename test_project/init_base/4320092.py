# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/27 23:02
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 计算圆周率。存在圆心在直角坐标系原点且半径为 1 的圆及其外切正方形。
# 为计算方便，仅考虑位于第一象限的四分之一正方形和四分之一圆。随机生成该四分之一正方形中一系列点，散布于四分之一圆内比例即为圆周率四分之一。散步点越多，结果越精确，耗时也越长。
#
# 以下程序实现了这一功能，请你填补空白处内容：
#
# from random import random
# from math import sqrt
# N=eval(input("请输入次数："))
# K=0
# for i in range(1,N+1):
# 	x,y=random(),random()
# 	dist =sqrt(x**2+y**2)
# 	_____________________;
# pi=4*(K/N)
# print("圆周率值：{}".format(pi))

from random import random
from math import sqrt

N = eval(input("请输入次数："))
K = 0
for i in range(1, N + 1):
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        K = K + 1
pi = 4 * (K / N)
print("圆周率值：{}".format(pi))
