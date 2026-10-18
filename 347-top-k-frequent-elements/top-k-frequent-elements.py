class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        ans = []

        for x in nums:
            freq[x] = freq.get(x,0)+1

        result = [[value,frequency] for value, frequency in freq.items()]
        result.sort(key = lambda x: (-x[1], x[0]))

        for i in range(k):
            ans.append(result[i][0])
        
        return ans


        
        