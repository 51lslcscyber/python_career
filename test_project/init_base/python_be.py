# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/ 4/ 7
# @version:1.10
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
if __name__ == '__main__':
    pass
# 一、循环遍历

# # 1.for循环遍历1-7去除4 c-practice 5
# for num in range(1, 8):
#     if num == 4:
#         continue
#     print(num)
# for num in range(1, 8):  # 为同时能运行两个循环，新取参数 num。
#     if num != 4:  # 当num != 4，执行打印语句；等于4时不打印。
#         print(num)

# # 2.while循环1-7去除4 c-practice 5
# n = 0
# while n < 7:
#     n = n+1
#     if n != 4:  # 当num != 4，执行打印语句；等于4时不打印。
#         print(n)

# password = ''  # 变量password用来保存输入的密码
#
# while password != '816':
#     password = input('请输入密码:')
# print('欢迎回家！')
# 3.简易模拟代码输入的功能

# # 4.换座问题 c-practice 5a
# students = ['小明', '小红', '小刚']
# for i in range(3):
#     student1 = students[0]  # 获取第一个座位的学生 student1
#     students = students[1:]  # 让 student1 暂时离开，后面的学生座位都进一位。
#     students.append(student1)  # 将 student1 安排到最后一个座位
#     print(students)

# # 5.判断 列表中是否有此 c-practice 6
# list = [1, 2, 3, 4, 5]
# a = 1
#
# # 做一次布尔运算，判断“a是否在列表list之中”
# print(bool(a in list))
# print(bool(a not in list))
