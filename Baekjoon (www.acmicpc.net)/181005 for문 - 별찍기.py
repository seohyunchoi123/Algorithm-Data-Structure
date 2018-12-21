n = int(input())

for i in range(n):
    n_star = n-i
    print(' '*i ,"*"*n_star, sep='')