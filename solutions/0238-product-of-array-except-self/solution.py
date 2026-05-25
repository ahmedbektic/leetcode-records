class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 2:
            ans = [nums[1], nums[0]]
            return ans
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i-1])
        
        suffix = ([0]*(len(nums)-1)) + [nums[len(nums)-1]]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = nums[i] * suffix[i+1]

        ans = [suffix[1]]
        for i in range(1, len(nums)-1):
            ans.append(prefix[i-1] * suffix[i+1])
        ans.append(prefix[len(nums)-2])
        return ans

