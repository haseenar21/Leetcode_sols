class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        min_len = float('inf')
        current_sum = 0

        for right in range(0,len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left+1)

                current_sum -=nums[left]
                left += 1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len