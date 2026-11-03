class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_alphanumeric(ch):
            code = ord(ch)
            return (48 <= code <= 57) or (65 <= code <= 90) or (97 <= code <= 122)

        left = 0
        right = len(s) - 1

        while left < right:
            if not is_alphanumeric(s[left]) :
                left += 1
                continue
            
            if not is_alphanumeric(s[right]) :
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                
            else:
                return False
        return True