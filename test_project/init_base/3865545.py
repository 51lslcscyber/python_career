# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/26 23:18
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
# 示例 1：
#
# 输入：s = "()"
# 输出：true
#
# 示例2：
#
# 输入：s = "()[]{}"
# 输出：true
#
# 示例3：
#
# 输入：s = "(]"
# 输出：false
#
# 示例4：
#
# 输入：s = "([)]"
# 输出：false
#
# 示例5：
#
# 输入：s = "{[]}"
# 输出：true
#
# 提示：
#
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = [
            '(', '[', '{',
            ')', ']', '}'
        ]
        i = 0
        sum = [0, 0, 0]
        top = []
        while i < len(s):
            c = s[i]
            j = 0
            while j <= 2:
                if c == parentheses[j]:
                    top.append(j)
                    sum[j] += 1
                elif c == parentheses[j + 3]:
                    if len(top) == 0 or top[len(top) - 1] != j:
                        return False
                    top.pop()
                    sum[j] -= 1
                j += 1
            i += 1
        if sum[0] != 0 or sum[1] != 0 or sum[2] != 0:
            return False
        else:
            return True


# %%
s = Solution()
print(s.isValid(s="()[]{}"))
