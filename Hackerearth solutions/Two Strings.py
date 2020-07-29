for _ in range(int(input())):
    s1, s2 = input().split()
    s3 = sorted(s1)
    s4 = sorted(s2)
    if s3 == s4:
        print("YES")
    else:
        print("NO")
