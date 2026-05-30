class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0 # looks for zero
        r = 0 # looks for non-zero
        b = False

        while (l != len(nums)) and (r != len(nums)):
            while nums[l] != 0:
                l += 1
                if l == len(nums):
                    b = True
                    break
            while nums[r] == 0:
                r += 1
                if r == len(nums):
                    b = True
                    break
            if b:
                break
            if l > r:
                r += 1
                continue # dont want to move zeroes to the left
            nums[l], nums[r] = nums[r], nums[l]

        return nums

        # while l < r:
        #     if nums[l] == 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         r -= 1
        #     else:
        #         l += 1

        [1,1,1,1,0,0,0,0]
