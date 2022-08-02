class Solution(object):
    def tribonacci(self, n):
        memo = [-1 for i in range(n+1)]
        return self.dp(n,memo)
        
    def dp(self,n,memo):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        if memo[n] != -1:
            return memo[n]
        memo[n] = self.dp(n-1,memo) + self.dp(n-2,memo) + self.dp(n-3,memo)
        return memo[n]