class Solution(object):
    def climbStairs(self, n):
        memo = [0 for i in range(n+1)]
        return self.dp(n,memo)
    def dp(self,n,memo):
        if n == 1 or n == 0:
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.dp(n-1,memo) + self.dp(n-2,memo)
        return memo[n]