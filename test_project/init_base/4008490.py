# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/6 16:44
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给出一串数字， 程序要把数字按照这样的格式输出，把连续增加的数字用 [x-y] 的形式表示，
# 只显示这一组顺序数字的首位两个数字，不连续增加的数字单独列出。
# 例如： 输入：1,2,3,4,5,8,10,11,12,13,20,21,22;输出：[1-5][8][10-13][20-22]。
seq = list(map(int, input().split(',')))
tmp = [seq[0]]
all_list = []
for n in range(len(seq)):
    if n == len(seq) - 1:
        all_list.append(tmp)
        break
    if seq[n + 1] - seq[n] == 1:
        tmp.append(seq[n + 1])
    else:
        all_list.append(tmp)
        tmp = [seq[n + 1]]
for a in all_list:
    if len(a) > 1:
        print('[%s-%s]' % (a[0], a[-1]))
    else:
        print('[%s]' % a[0])