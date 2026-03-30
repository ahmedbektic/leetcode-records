class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        
        # consider how many ways to reach last step starting at the step right before it
        dp = [0] * (n-1)
        dp[n-2] = 1
        dp[n-3] = 2

        for i in range(n-4, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]

        return dp[0] + dp[1]

        
