# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/11 22:17
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 定义一个名为“isStrongPassword”的函数，该函数将字符串作为参数。
# 功能然后将检查所提供的字符串是否满足以下条件，以检查是否为强 密码：
# 1.必须至少包含1个大写和小写字母的组合 2.必须至少包含3位数字 3.必须至少包含3个特殊字符（包括空格）
# 4.密码长度必须至少12个字符 该函数将返回一个布尔值，即如果满足所有条件则返回True或返回False
# 确保使用可能返回False值的每个可能的输入来测试函数也一样
def isStrongPassword(pwd):
    chars = list(pwd)
    upper = [c for c in chars if 'A' <= c <= 'Z']
    lower = [c for c in chars if 'a' <= c <= 'z']
    digit = [c for c in chars if '0' <= c <= '9']
    symbol = [c for c in chars if not (
                'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9')]
    strong = len(upper) >= 1 and len(lower) >= 1 and len(digit) >= 3 and len(
        symbol) >= 3 and len(pwd) >= 12
    return strong


print(isStrongPassword("Str0n9P@$$w0rd"))
print(isStrongPassword("StrongPassword"))
print(isStrongPassword("Stron9P@$$0rd"))
print(isStrongPassword("Str0n9Pass0rd"))
print(isStrongPassword("str0n9p@$$0rd"))
print(isStrongPassword("Str0n9P@$$"))
print(isStrongPassword("12345678"))
print(isStrongPassword("~!@#$$%^&*()_+"))
print(isStrongPassword("STRONGPASSWORD"))
