class Solution(object):
    def twoSum(self,nums, target):
        freq = {}
        seen = {}
        result = []
        complement = 0
        n = len(nums)
        for i in range(0,n):
            complement = target - nums[i]
            if complement not in seen:
                seen[nums[i]] = i
            else:
                result.append(i)
                result.append(seen[complement])
                break
        return result




            


