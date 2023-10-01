class Solution(object):
    def smallestEvenMultiple(self, n):
        i=2
        while True:   
            if i % n == 0:
                return i
            else:
                i += 2
            
        
