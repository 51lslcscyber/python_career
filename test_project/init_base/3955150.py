# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/1 11:07
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
# 提示：
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
def subsets(nums):
    allset = 2 ** len(nums)
    result = []
    for i in range(allset):
        item = []
        for j in range(len(nums)):
            if i & (2 ** j):
                item.append(nums[j])
        result.append(item)
    return result


class Solution:
    pass


if __name__ == "__main__":
    s = Solution()
    print(subsets([1, 2, 3]))
