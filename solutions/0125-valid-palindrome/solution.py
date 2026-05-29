class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = ""
        for char in s:
            if char.isalnum():
                st += char.lower()

        l = 0
        r = len(st)-1
        for i in range(len(st) // 2):
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        
        return True
