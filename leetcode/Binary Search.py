"""
Given a sorted (in ascending order) integer array nums of n elements and a 
target value, write a function to search target in nums. If target exists, 
then return its index, otherwise return -1.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        now = 0
        while now < len(nums):
            if nums[now] == target:
                return(now)
            now += 1
        return(-1)