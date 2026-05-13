class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = dict()
        for char in s:
            if char in chars:
                chars[char] += 1
            else: chars[char] = 1
        
        hasOdd = False
        pairs = 0
        
        for value in chars.values():
            if not hasOdd:
                if value % 2 == 1:
                    hasOdd = True
            pairs += (value // 2)

        return 2*pairs + int(hasOdd)
        
