n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
count = 0
for i in arr:
    if k - i >= 0:
        count += 1
        k -= i
print(count)
