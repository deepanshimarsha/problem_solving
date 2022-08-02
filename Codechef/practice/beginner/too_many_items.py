def polybags(t):
    for i in range(0,t):
        items = int(input())
        if items % 10 == 0:
            print(items // 10)
        else:
            print(items//10 + 1)

t = int(input())
polybags(t)

