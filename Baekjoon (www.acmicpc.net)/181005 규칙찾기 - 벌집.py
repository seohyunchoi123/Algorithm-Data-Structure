# 벌집
def cal(k):
    if k==0:
        return -1
    elif k==1:
        return 1
    else:
        return 3*k*(k-1) +1

n = int(input())
for i in range(2*n):
    if n<= cal(i):
        break
print(i)