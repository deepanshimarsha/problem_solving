def pass_fail(t):
    for i in range(0,t):
        n, x, p = map(int, input().split())
        right = x*3
        wrong = (n-x)*1
        total = right-wrong
        if total >= p:
            print("PASS")
        else:
            print("FAIL")

t = int(input())
pass_fail(t)