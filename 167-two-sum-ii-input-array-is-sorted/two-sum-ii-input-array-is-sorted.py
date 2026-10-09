class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right] 

            if target == current_sum:
                return [left+1,right+1]
            elif target < current_sum:
                right -= 1
            
            elif target > current_sum:
                left += 1
            
            