def blackjack(t):
    for i in range(0,t):
        a, b = map(int,input().split())
        c = 21 - (a+b)
        if c in range(1,11):
            print(c)
        else:
            print(-1)

t = int(input())
blackjack(t)
