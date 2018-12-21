m = int(input())
n= int(input())

def checking(num):
    is_sosu =1
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            is_sosu=0
    if is_sosu==1:
        return True
    else:
        return False
result=[]
for i in range(m, n+1):
    if checking(i) ==True:
        result.append(i)
if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(result[0])