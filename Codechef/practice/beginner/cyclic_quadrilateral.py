def cyclic_quadrilateral(t):
    for i in range(0,t):
        a, b, c, d = map(int, input().split())
        if a + c == 180 and b + d == 180:
            print("YES")
        else:
            print("NO")

t = int(input())
cyclic_quadrilateral(t)