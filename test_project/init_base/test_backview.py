# -*- coding: utf-8 -*-

# @Time:2021/10/06
# @version:
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: 
# run again.  Do not edit this file unless you know what you are doing.
# 文件操作面试失误题
# 文件操作1
# 1.生成一个文件file1,每一行随机生成5个数字,数字之间用逗号隔开
# 2.读取文件file1,计算并输出每一行数字的总和
# 写文件.
import random
lines = 10
num = 1000000
nums = 5
per_write = ''
for i in range(lines):
    num_list = []
    for i in range(nums):
        n = random.randint(0, num)
        num_list.append(str(n))
    per_write += ','.join(num_list) + '\n'
with open('./file1.txt', 'w', encoding='utf-8') as file1:
    file1.write(per_write)


# 读文件
with open('./file1.txt', 'r', encoding='utf-8') as file2:
    read_str = file2.read()
file2_lines = read_str.split('\n')[:-1]
sums_dict = {}
for i in file2_lines:
    sums_dict[file2_lines.index(i)] = sum(list(eval(i)))
print(sums_dict)

if __name__ == "__main__":
    pass
