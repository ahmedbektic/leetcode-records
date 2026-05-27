class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = list(s)
        total = 0
        prev = s[len(s)-1]
        total += dic[s[len(s)-1]]
        s.pop()

        while s:
            while s and dic[s[len(s)-1]] < dic[prev]:
                total -= dic[s[len(s)-1]]
                s.pop()

            if s and dic[s[len(s)-1]] >= dic[prev]:
                prev = s[len(s)-1]
                total += dic[s[len(s)-1]]
                s.pop()
        
        return total


        
