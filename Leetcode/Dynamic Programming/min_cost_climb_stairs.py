def minCostClimbingStairs(cost):
    cost.append(0)
    n = len(cost)
    c = cost[n-1] 
    memo = [-1 for i in range(n+1)]
    return dp(cost,memo,n,c)
    
    
def dp(cost,memo,n,c):
    if n == 1 or n == 2:
        return c
    if memo[n] != -1:
        return memo[n]
    memo[n] = min(dp(cost,memo,n-1,c+cost[n-2]),dp(cost,memo,n-2,c+cost[n-3]))
    return memo[n]

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
        
    