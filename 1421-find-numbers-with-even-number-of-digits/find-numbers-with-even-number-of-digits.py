class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        even = 0
        for i in range(0,n):
            for j in range(0,10):
                m = math.pow(10,j)
                if nums[i]/ m < 10 and nums[i]/m >= 1 and j%2 == 1:
                    even += 1
                    break
        return even