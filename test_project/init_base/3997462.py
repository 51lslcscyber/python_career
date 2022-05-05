# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/5 13:47
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
# num1和num2的长度小于110。
# num1 和num2 只包含数字0-9。
# num1 和num2均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    res = ''
    ls1, ls2, = len(num1), len(num2)
    ls = ls1 + ls2
    arr = [0] * ls
    for i in reversed(range(ls1)):
        for j in reversed(range(ls2)):
            arr[i + j + 1] += int(num1[i]) * int(num2[j])
    for i in reversed(range(1, ls)):
        arr[i - 1] += arr[i] / 10
        arr[i] %= 10
    pos = 0
    if arr[pos] == 0:
        pos += 1
    while pos < ls:
        res = res + str(arr[pos])
        pos += 1
    return res


class Solution(object):
    pass


if __name__ == '__main__':
    s = Solution()
    print(multiply("123", "456"))
