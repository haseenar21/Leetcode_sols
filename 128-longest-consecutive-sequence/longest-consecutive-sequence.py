class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        seen = set()
        count = set()
        if len(nums) == 0:
            return 0 
        for x in nums:
            if x-1 not in nums:
                seen.add(x)

        for x in seen:
            final_x = set()
            while True:
                if x+1 in nums:
                    if x not in final_x:
                        final_x.add(x)
                    if x+1 not in final_x:
                        final_x.add(x+1)
                        x = x+1
                else:
                    final_x.add(x)
                    count.add(len(final_x))
                    break
        return max(count)
        








        
