def examtime(t):
    for i in range(t):
        dragon = list(map(int,input().split()))
        sloth = list(map(int,input().split()))

        sum_d = sum(dragon)
        sum_s = sum(sloth)

        if sum_d >sum_s:
            print("DRAGON")

        elif sum_s > sum_d:
            print("SLOTH")

        else:
            if dragon[0] > sloth[0]:
                print("DRAGON")
            elif dragon[0] < sloth[0]:
                print("SLOTH")
            else:
                if dragon[1] > sloth[1]:
                    print("DRAGON")
                elif dragon[1] < sloth[1]:
                    print("SLOTH")
                else:
                    print("TIE")

        
        
        
t = int(input())
examtime(t)