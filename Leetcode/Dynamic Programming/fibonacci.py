#n = int(input())
n = 4
memo = [-1 for i in range(n+1)]
def fib(n):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = n*fib(n-1)
    return memo[n]

print(fib(n))