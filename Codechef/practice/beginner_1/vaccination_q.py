def vaccinq(t):
    for i in range(t):
        n,p,x,y = map(int,input().split())
        idx = list(map(int,input().split()[:n]))
        time = 0
        for j in range(p):
            if idx[j] == 0:
                time += x
            else:
                time += y
        print(time)

t = int(input())
vaccinq(t)