def atm2(t):
    for i in range(t):
        n, k = map(int,input().split())
        a = list(map(int,input().split()))
        s = ""
        for amt in a:
            if k-amt >= 0:
                k = k - amt
                s += "1"

            else:
                s += "0"
        print(s)
t = int(input())
atm2(t)

