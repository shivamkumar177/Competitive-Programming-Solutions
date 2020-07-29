N = int(input())
count = 0
for i in range(N):
    n = int(input())
    for i in range(33):
        if 2**i == n:
            count += 1
print(count)
