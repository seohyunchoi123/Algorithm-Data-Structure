n = input()
n = map(int,list(n))
n= sorted(n)[::-1]
for t in n:
    print(t,end='')