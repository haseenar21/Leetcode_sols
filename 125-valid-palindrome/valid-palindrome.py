class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pal = ""
        clean_arr = ""
        lower_arr = s.lower()
        rem_spac_arr = lower_arr.replace(" ","")
        for char in rem_spac_arr:
            if char.isalnum():
                clean_arr += char
        n = len(clean_arr)
        for i in range(n-1,-1,-1):
            pal+=clean_arr[i]
        if clean_arr == pal:
            return True
        else:
            return False
