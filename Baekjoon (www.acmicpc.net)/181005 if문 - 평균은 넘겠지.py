# 평균은 넘겠지

T = int(input())
result=[]

for _ in range(T):
    t = list(map(int,input().split()))
    num=t[0]
    scores = t[1:]
    avg = sum(scores)/num

    cnt=0
    for t in scores:
        if t > avg:
            cnt+=1
    prop = str(round(cnt/num*100, 3))
    while True:
        if len(prop.split('.')[1]) < 3:
            prop += '0'
        else :
            break
    result.append(prop + '%')

for t in result:
    print(t)