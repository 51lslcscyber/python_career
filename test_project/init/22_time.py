# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/6 9:23
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 以下代码段可用于计算执行特定代码所需的时间。
import time

start_time = time.time()
a = 1
b = 2
c = a + b
print(c)  # 3
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)
# ('Time: ', 1.1205673217773438e-05)
