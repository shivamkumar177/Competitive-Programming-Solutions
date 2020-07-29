n, x = map(int,input().split())
c = 0
arr = list(map(int,input().split()))
 
for i in range(n):
    c += 1
    x -= arr[i]
    if x<0:
        print(c)
        break
