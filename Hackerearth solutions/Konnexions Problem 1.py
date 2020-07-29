n,m = map(int,input().split())
if m%n == 0:
    print(0)
else:
    print(n-m%n)
