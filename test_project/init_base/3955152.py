# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/1 11:15
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
# 给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标。
#
# 示例1：
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#
# 示例2：
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# 0 <= nums[i] <= 105
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    length = len(nums)
    begin = length - 1
    for i in reversed(range(length - 1)):
        if i + nums[i] >= begin:
            begin = i
    return not begin


class Solution(object):
    pass


# %%
s = Solution()
print(canJump(nums=[2, 3, 1, 1, 4]))
print(canJump(nums=[3, 2, 1, 0, 4]))
