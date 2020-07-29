m =int(input())
b = int(input())
n = int(input())
res = 0
for _ in range(n):
    c,a = map(str,input().split())
    a = int(a)
    if c == "D":
        print(b+a)
        b += a
    elif c == "W" and b >= m:
        res = b - a
        if res >=m:
            print(res)
            b -= a
        else:
            print("Cannot withdraw!")
