n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
res = []
for i in range(n):
    res.append(A[i]+B[i])
print(*res)
