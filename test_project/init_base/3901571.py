# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/28 23:02
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 实现保留3位有效数字（四舍六入五成双规则） 输入：1234
# 输出：1234 12 12.0 4 4.00 0.2 0.200
# 0.32 0.320 1.3 1.30 1.235 1.24 1.245 1.24 1.2451 1.25
a = input()
if '.' in a:
    a = float(a)
    if a * 1000 % 10 != 5:
        a = '%.2f' % (a)
    else:
        if len(str(a).split(".")[1]) > 3:
            a = '%.2f' % (a)
        else:
            if int(a * 100 % 10 % 2) == 1:
                a = float('%.2f' % float(int(a * 100) / 100)) + 0.01
            else:
                a = '%.2f' % float(int(a * 100) / 100)
    print(a)
else:
    a = int(a)
    if a > 99:
        print(a)
    else:
        if 0 < a < 10:
            print('%.2f' % a)
        else:
            print(float(a))
