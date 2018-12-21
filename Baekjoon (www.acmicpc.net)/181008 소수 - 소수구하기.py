a,b = list(map(int,input().split()))

# for num in range(a,b+1):
#     is_sosu=1
#     for i in range(2,num):
#         if num%i==0:
#             is_sosu=0
#             break
#     if is_sosu==1:
#         print(num)    # 시간초과

board = list(range(b+1)) # set으로 해서 하나씩 뺴지말고 list로 해서 하나씪 수를 -1로 바꿔줘라

for i in range(2,b):
    for j in range(2,b//2):
        t =i*j
        if t>b:
            break
        board[t]=-1
for t in board[a:]:
    if t!= -1 and t!= 1 : # 이렇게는 또 안되네
        print(t)    # 정답 ! >> set을 이용해서 그떄마다 빼는 식으로 하면 시간초과뜨네 ! set이 느린가보다