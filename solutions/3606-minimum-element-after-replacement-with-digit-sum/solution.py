class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            j = 1
            if nums[i] < 10:
                continue
            digits = []
            while nums[i] >= j:
                j *= 10
                digit = (nums[i] % j) / (j/10)
                digits.append(int(digit))
                if nums[i] < digit:
                    break
                nums[i] -= digit
            nums[i] = sum(digits)
        return min(nums)
