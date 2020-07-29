for _ in range(int(input())):
    n, k = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(int,input().split()))[:n]
    small = min(arr)
    if k>small:
        print(k-small)
    else:
        print("0")
