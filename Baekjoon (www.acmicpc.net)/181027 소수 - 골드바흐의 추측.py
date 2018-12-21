import sys
T= int(sys.stdin.readline())
m=10000
result=[]
board = list(range(m)) # board는 무조건 밖으로 뺴자
board[0] = 0; board[1] = 0; board[m-1] = 0
for i in range(2, m//2):
    for j in range(2,m//i+1):
        if i*j>=m:
            break
        board[i*j]=0
# print(board)
for _ in range(T):
    n = int(sys.stdin.readline())

    for i in range(int(n/2),n):
        j = n-i
        if board[i] and board[j]: # i in prime and j in prime을 이렇게만 바꾸니까 엄청나게 빨라졋다 ....
            # print(board[i], board[j])
            result.append([j,i])
            break
for t in result:
    print(t[0], t[1])
