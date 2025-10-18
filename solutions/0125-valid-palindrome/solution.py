class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        #isalnum refers alphanumeric, isalpha refers alphabetic... isnumeric

        l = 0
        r = len(cleaned)-1

        while (l < r):
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True

        

        
