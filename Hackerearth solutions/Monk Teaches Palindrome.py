for _ in range(int(input())):
    s = input()
    if s[::-1]==s:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
