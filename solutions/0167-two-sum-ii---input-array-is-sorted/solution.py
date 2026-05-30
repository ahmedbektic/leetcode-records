class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1
        # while numbers[r] > target:
        #     r -= 1
        while numbers[l] + numbers[r] != target:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            else:
                l += 1
        if l > r:
            l, r = r, l
        return [l+1, r+1]
        
