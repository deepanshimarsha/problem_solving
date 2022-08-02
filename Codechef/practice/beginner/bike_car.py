def faster(T):
    for i in range(0,T):
        b, c = map(int,input().split())
        if b < c:
            print("BIKE")
        elif b > c:
            print("CAR")
        else:
            print("SAME")

T = int(input())
faster(T)



    
