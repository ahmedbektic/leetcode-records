class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashed = set(nums)
        for num in hashed:
            if (target - num) in hashed:
                first = nums.index(num)
                nums[first] = None
                if (target - num) in nums:
                    return [first, nums.index(target - num)]
