class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) in [0,1]:
            return len(s)
        
        last = len(s)
        p1 = 0
        p2 = 0
        seen = {s[p1]}
        n = 1

        while p2 < last-1:
            p2 += 1
            if s[p2] in seen:
                while (s[p1] != s[p2]) and (p1 != p2):
                    seen.remove(s[p1])
                    p1 += 1
                seen.remove(s[p1])
                p1 += 1
            seen.add(s[p2])
            n = max(n, len(seen))

        return n
                
            


        
