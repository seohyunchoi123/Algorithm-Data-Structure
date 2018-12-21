def check_sosu(n):
    board = list(range(n+1)) # 0 ~ n 까지의 리스트
    for i in range(2,n):
            for j in range(1,len(board)):
                idx = i*j
                if idx > n:
                    break
                board[idx]=-1
                if board[n]==-1:
                    return False
    return True
