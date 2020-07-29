s = input()
b = s.rsplit(' ', 1)[0]
word = s.split(' ')
print('. '.join([x[0] for x in b.split()]),". ",sep='',end='')
print(word[-1])
