class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        window = ""
        max_len = float('-inf')
        while len(s) > 0:
            for right in range(len(s)):
                if s[right] not in window or not window:
                    window += s[right]
                    max_len = max(max_len, right - left+1)
                else:
                    while s[right] in window:
                        left += 1
                        window = window [1 : ]
                    window += s[right]
    
            return max_len
        return 0