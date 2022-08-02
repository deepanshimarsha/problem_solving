def proglang(t):
     for _ in range(t):
        flag = 0
        features = list(map(int, input().split()[:6]))
        A, B = features[0], features[1]
        for i in range(2, len(features)-1, 2):
            if A == features[i] and B == features[i+1] or A == features[i+1] and B == features[i]:
                print(i//2)
                flag = 1
                break
        
        if flag == 0:
            print(0)

t = int(input())
proglang(t)

