# -*- coding: utf-8 -*-

# @Time:2022/0/
#@version:
# Created by: Python3.9.6
#@author:鹄思鹄想bit森
# WARNING: run again.  Do not edit this file unless you know what you are doing.
'''
寻找旋转排序数组中的最小值
'''
nums=[3,4,5,1,2]
class Solution(object):
    def findmin(self,nums):
        flag=True
        if nums[0]<nums[-1]:
            flag=False
        else:
            flag=False
        for i in range(1,len(nums)):
            if flag:
                if nums[i]<nums[i-1]:
                    return nums[i]
            else:
                if nums[len(nums)-i]<nums[len(nums)-1-i]:
                    return nums[len(nums)-i]
        return nums[0]
print(nums)