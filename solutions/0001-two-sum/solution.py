class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = dict()
        for i, num in enumerate(nums):
            if ((target - num) in checked):
                return [checked.get(target - num), i]
            checked.update({num:i})

        
