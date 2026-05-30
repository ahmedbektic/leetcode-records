class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        for h, char in enumerate(haystack[0:len(haystack)-len(needle)+1]):
            if char != needle[0]:
                continue
            j = h
            n = 0
            match = True
            for i in range(len(needle)):
                if needle[n] != haystack[j]:
                    match = False
                    break
                n += 1
                j += 1
            if match:
                return h
        return -1

        
