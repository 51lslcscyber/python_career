# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/21 9:31
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入:n = 4, k = 2
# 输出:[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],]
class Solution(object):
    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 1)
        return res

    def get_combine(self, res, prefix, n, k, start):
        if k == 0:
            res.append(list(prefix))
        elif start <= n:
            prefix.append(start)
            self.get_combine(res, prefix,
                             n, k - 1, start + 1)
            prefix.pop()
            self.get_combine(res, prefix,
                             n, k, start + 1)


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
