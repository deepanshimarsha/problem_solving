def valentine(t):
    for i in range(0,t):
        x, y = map(int,input().split())
        print(x//y)

t = int(input())
valentine(t)