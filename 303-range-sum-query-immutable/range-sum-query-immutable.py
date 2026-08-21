class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        runningSum = 0
        n = len(nums)
        self.prefix = []
        
        for i in range(0,n):
            runningSum += nums[i]
            self.prefix.append(runningSum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return (self.prefix[right])
        else:
            return (self.prefix[right]-self.prefix[left-1])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)