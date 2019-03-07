class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        now = 0
        while now < len(nums):
            if nums[now] == target:
                return(now)
            elif nums[now] < target:
                now += 1
            else:
                return(now)
        return(len(nums))