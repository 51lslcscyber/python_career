# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/18 15:04
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.



def fractionToDecimal(numerator, denominator):
    if numerator >= 0 and denominator >= 0:
        numerator, denominator = -numerator, -denominator
    u = (numerator < 0) ^ (denominator < 0)
    numerator = abs(numerator)
    denominator = abs(denominator)
    numerator = numerator % denominator
    if numerator == 0:
        return str(numerator // denominator)
    s = str(abs(numerator) // denominator) + "."
    q = {}
    l = []
    while numerator < denominator:
        numerator = numerator * 10
        l.append(numerator)
        q[numerator] = numerator // denominator
    numerator = numerator % denominator * 10
    while numerator not in q and numerator != 0:
        l.append(numerator)
        q[numerator] = numerator // denominator
        numerator = numerator % denominator
        numerator = numerator * 10
    for i in range(0, len(l)):
        if numerator == l[i]:
            s = s + "("
        s = s + str(q[l[i]])
    if "(" in s:
        s = s + ")"
    if u:
        s = "-" + s
    return s


class Solution(object):
    pass


if __name__ == "__main__":
    s =Solution
    print(p=s.__flags__)
    pass
