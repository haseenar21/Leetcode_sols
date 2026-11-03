class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1

        while l<r:
            nums[l] = nums[l]*nums[l]
            nums[r] = nums[r]*nums[r]
            l += 1
            r -= 1
        if l == r:
            nums[l] = nums[l]*nums[l]
        nums.sort()
        return nums
