class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}

        for w in s:
            freq[w] = freq.get(w,0) + 1

        for i in range(0,len(s)):
            if freq[s[i]] == 1:
                return i
        return -1