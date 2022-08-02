def muffinpackaging(t):
    for i in range(t):
        n = int(input())
        max_r = 0
        for j in range(1,n+1):
            r = n % j
            max_r = max(r,max_r)

        print(n-max_r)

t = int(input())
muffinpackaging(t)

