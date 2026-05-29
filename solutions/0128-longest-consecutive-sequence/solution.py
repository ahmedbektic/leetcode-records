class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        longest = 1
        s = set(nums)
        
        for num in s:
            # only consider starting elements
            if (num-1) not in s:
                counter = 1
                n = num
                while (n+1) in s:
                    counter += 1
                    n += 1
                longest = max(counter, longest)
        
        return longest
