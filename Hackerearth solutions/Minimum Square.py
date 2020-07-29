for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    brr = []
    for i in arr:
        i = abs(i)
        brr.append(i)
    print((min(brr))**2)
