# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/24 16:23
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
#
# 示例1:
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
# 示例2:
#
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
#
# 说明:
#
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        n = len(nums) + 1
        step = (max_val - min_val) // n
        exist = [0 for _ in range(n + 1)]
        max_num = [0 for _ in range(n + 1)]
        min_num = [0 for _ in range(n + 1)]
        for num in nums:
            idx = self.findBucketIndex(num, min_val, max_val, n)
            max_num[idx] = num if not exist[idx] else max(num, max_num[idx])
            min_num[idx] = num if not exist[idx] else min(num, min_num[idx])
            exist[idx] = 1
        res = 0
        pre = max_num[0]
        for i in range(1, n + 1):
            if exist[i]:
                res = max(res, min_num[i] - pre)
                pre = max_num[i]
        return res

    def findBucketIndex(self, num, min_val, max_val, n):
        return int((num - min_val) * n % (max_val - min_val))


if __name__ == "__main__":
    pass
