def fundstatus(T):
    for i in range(0,T):
        A, B, x, y = map(int,input().split())
        if (A*B) <= (x*y):
            print("yes")
        else:
            print("no")

T = int(input())
fundstatus(T)