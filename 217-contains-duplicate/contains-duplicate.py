class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        return False
        