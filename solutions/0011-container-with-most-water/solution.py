class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        m = 0
        while l != r:
            size = (r-l) * min(height[l], height[r])
            m = max(m, size)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m
        
