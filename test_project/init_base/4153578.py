# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/15 18:16
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 要求编写函数fn(a,n) 求a+aa+aaa++⋯+aa⋯aa(n个a）之和，fn须返回的是数列和。
# 从控制台输入正整数a和n的值（两个值都不超过9），并输出fn(a,n)的结果值。
def fun(a, n):
    s = 1
    sum = 1
    for i in range(1, n):
        s = 1 + s * 10
        sum += s
    y = a * sum
    print(y)


def main():
    while (1):
        a = int(input('请输入a:'))
        if a > 9 or a < 0:
            print('a的值输入错误，请重新输入：')
        else:
            break
    while (1):
        n = int(input('请输入n:'))
        if n > 9 or n < 0:
            print('n的值输入错误，请重新输入：')
        else:
            break
    fun(a, n)


if __name__ == '__main__':
    main()