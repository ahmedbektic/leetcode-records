class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ptr = 0
        rCount = 0
        lCount = 0
        maximum = 0

        # while substring is imbalanced or empty (and ptr is in range)
        while (rCount != lCount or rCount + lCount == 0) and (ptr < len(s)):
            if s[ptr] == "R":
                rCount += 1
            else:
                lCount += 1
            
            ptr += 1

            # if substring is balanced and non-empty
            if rCount == lCount and rCount + lCount != 0:
                rCount = 0
                lCount = 0
                maximum += 1
        
        return maximum




        
