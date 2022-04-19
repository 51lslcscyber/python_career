# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/19 22:13
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组nums中。
#
# 现在要求你戳破所有的气球。
# 戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
# 这里的 i - 1 和 i + 1 代表和i相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
#
# 求所能获得硬币的最大数量。
#
# 示例 1：
#
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# 示例 2：
#
# 输入：nums = [1,5]
# 输出：10
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100
from typing import List


def maxCoins(nums: List[int]) -> int:
    n = len(nums) + 2
    nums = [1] + nums + [1]
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if j - i > 1:
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k][j] + nums[i] * nums[
                                       k] * nums[j])
    return dp[0][n - 1]


class Solution:
    pass


if __name__ == "__main__":
    pass
