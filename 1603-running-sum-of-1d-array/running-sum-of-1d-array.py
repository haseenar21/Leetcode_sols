class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        n = len(nums)
        for i in range(0,n):
                sum += nums[i]
                nums[i] = sum
        return nums