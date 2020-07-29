for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    num = min(arr)
    count = 0
    for i in arr:
        if i == num:
            count += 1
    if count%2 == 0:
        print("Unlucky")
    else:
        print("Lucky")
