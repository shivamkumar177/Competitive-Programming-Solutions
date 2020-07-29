from collections import Counter
for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        c = Counter(arr)
        for i in arr:
                if c[i] == 1:
                        print(i)
