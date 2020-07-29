s1 = input()
s2 = input()
if len(s1) == len(s2):
    if set(s1) == set(s2):
        print("true")
    else:
        print("false")
else:
    print("false")
