# T = int(input())
# result=[]
# for _ in range(T):
#     m, n, x, y = list(map(int,input().split()))
#     a,b= 0, 0
#     is_finding=0
#     for  i in range(m*n):
#         a+=1 ; b+=1
#         if a > m:
#             a=1
#         if b > n :
#             b=1
#         ans = str(a)+str(b)
#         if ans == (str(x)+str(y)):
#             is_finding=1
#             break
#     if is_finding==1:
#         result.append(i+1)
#     else:
#         result.append(-1)
#
# for t in result:
#     print(t)

# T = int(input())
# result=[]
# for _ in range(T):
#     m, n, x, y = list(map(int,input().split()))
#     is_finding=0
#     for i in range(m*n):
#         i+=1
#         if i%m ==x and i%n ==y:
#             is_finding+=1
#             break
#     if is_finding==1:
#         result.append(i)
#     else:
#         result.append(-1)
# for t in result:
#     print(t)


T = int(input())
result=[]
for _ in range(T):
    m, n, x, y = list(map(int,input().split()))
    is_finding=0
    for i in range(n):
        candidate = m*i + x
        # if candidate%n ==y : # 10 12 10 12 일 경우
        #     is_finding+=1
        #     break
        # elif candidate%n ==0 and n==y:
        #     is_finding+=1
        #     break
        if candidate%n ==y or (candidate%n==0 and n==y):
            is_finding+=1
            break
    if is_finding==1:
        result.append(candidate)
    else:
        result.append(-1)
for t in result:
    print(t)

# if x%n ==y or (x%n==0 and n==y) #? 될까?