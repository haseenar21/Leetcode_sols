class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s = {}
        for x in s:
            freq_s[x] = freq_s.get(x,0)+1
        
        freq_t = {}
        for x in t:
            freq_t[x] = freq_t.get(x,0)+1

        if freq_s == freq_t and len(s) == len(t):
            return True
        else:
            return False

        