for _ in range(int(input())):
    c,t,l = map(int,input().split())
    f = 1
    if l%4 != 0:
        print("no")
        continue
    if (l-t*4)<0:
        print("no")
        continue
    l = l - t*4;
    if l<((c-2*t)*4):
        print("no")
    elif(l>0):
        while c>0 and l>0:
            if l==2:
                print("no")
                f = 0
                break
            l-=4
            c-=1
        if f==1 and l<=0:
            print("yes")
        elif f==1:
            print("no")
    else:
        print("yes")
