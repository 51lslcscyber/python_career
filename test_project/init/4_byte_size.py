# -*- coding: utf-8 -*-

# @Time:2022/4/19
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.
# Do not edit this file unless you know what you are doing.
# 计算字节大小
def byte_size(string):
    return (len(string.encode('utf-8')))


if __name__ == "__main__":
    print(byte_size('集群'))
    print(byte_size('🐅'))
    print(byte_size('🐉'))
    pass
