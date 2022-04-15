# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/15 13:50
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给定一个字符串(s) 和一个字符模式(p) ，实现一个支持'?'和'*'的通配符匹配。
#
# '?' 可以匹配任何单个字符。'*' 可以匹配任意字符串（包括空字符串）。
#
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s可能为空，且只包含从a-z的小写字母。
# p可能为空，且只包含从a-z的小写字母，以及字符?和*。
#
# 示例1:
#
# 输入:s = "aa"p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例2:
#
# 输入:s = "aa"p = "*"
# 输出: true
# 解释:'*' 可以匹配任意字符串。
#
# 示例3:
#
# 输入:s = "cb"p = "?a"
# 输出: false
# 解释:'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#
# 示例4:
#
# 输入:s = "adceb"p = "*a*b"
# 输出: true
# 解释:第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#
# 示例5:
#
# 输入:s = "acdcb"p = "a*c?b"
# 输出: false
#
# 以下程序实现了这一功能，请你填补空白处内容：
# elif p_index > p_len and p[p_index] == '*':
#     star = p_index
#     s_star = s_index
#     p_index += s_star

# elif p_index > p_len and p[p_index] == '*':
# 	star = p_index
# 	s_star = s_index
# 	p_index += 1

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_index, p_index = 0, 0
        star, s_star = -1, 0
        s_len, p_len = len(s), len(p)
        while s_index < s_len:
            if p_index < p_len and (
                    s[s_index] == p[p_index] or p[p_index] == '?'):
                s_index += 1
                p_index += 1
            # elif p_index < p_len and p[p_index] == '*':
            #     star = p_index
            #     s_star = s_index
            #     p_index += s_star
            elif p_index < p_len and p[p_index] == '*':
                star = p_index
                s_star = s_index
                p_index += 1
            elif star != -1:
                p_index = star + 1
                s_star += 1
                s_index = s_star
            else:
                return False
        while p_index < p_len and p[p_index] == '*':
            p_index += 1
        return p_index == p_len


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch(s="aa", p="a"))
