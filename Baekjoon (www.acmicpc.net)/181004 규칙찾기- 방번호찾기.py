# 방 번호 찾기
n = list(input().replace('9','6'))

result=0
while True:
    dic = list('1234566780')
    n_copy = n.copy()
    for t in n_copy:
        if t in dic:
            dic.pop(dic.index(t))
            n.pop(n.index(t))
        else:
            continue
    result +=1
    if  len(n)==0:
        break
print(result)

