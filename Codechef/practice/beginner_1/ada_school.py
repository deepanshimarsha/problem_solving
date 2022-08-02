def adaschool(t):
    for i in range(t):
        n, m = map(int,input().split())
        if m % 2 == 0:
            print("YES")
        else:
            if n % 2 == 0:
                print("YES")
            else:
                print("NO")
        
t = int(input())
adaschool(t)