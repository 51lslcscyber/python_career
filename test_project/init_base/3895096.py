# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/27 23:09
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 本题要求两个给定正整数的最大公约数和最小公倍数。
# 输入格式:
#
# 输入在两行中分别输入正整数x和y。
#
# 输出格式:
#
# 在一行中输出最大公约数和最小公倍数的值。
#
#
#
# 输入样例1:
#
# 在这里给出一组输入。
#
# 例如：
#
# 100
# 1520
#
# 输出样例1:
#
# 在这里给出相应的输出。
#
# 例如：
#
# 20 7600
#
# 以下程序实现了这一功能，请你填补空白处内容：
#
# def hcf(x, y):
#    if x > y:
# 	   smaller = y
#    else:
# 	   smaller = x
#    for i in range(1,smaller + 1):
# 	   if((x % i == 0) and (y % i == 0)):
# 		   hcf = i
#    return hcf
# def lcm(x, y):
#    if x > y:
# 	   greater = x
#    else:
# 	   greater = y
#    while(True):
# 	   ____________________;
# 	   greater += 1
#    return lcm
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
# print("最大公约数为",hcf(num1, num2),"最小公倍数为",lcm(num1,num2))
def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) or (greater % y == 0)):
            lcm = greater
            break
            greater += 1
    return lcm


num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print("最大公约数为", hcf(num1, num2), "最小公倍数为", lcm(num1, num2))
