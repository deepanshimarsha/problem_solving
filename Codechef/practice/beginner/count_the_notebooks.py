def count_notebooks(T):
    for i in range(0,T):
        weight = int(input())
        pages = weight * 1000
        num = pages // 100
        print(num)

T = int(input())
count_notebooks(T)