# 콘웨이의 생명 게임(Conway's game of life)은 영국의 수학자 존 호튼 콘웨이가 고안해낸 세포 자동자 게임이다. 바둑판처럼 정사각형의 여러 칸으로 나뉘어진 공간에서 한 칸에 한 마리씩 있는 세포들의 삶과 죽음이 펼쳐지는 게임이라 할 수 있다. 규칙은 단순하지만 만들어 낼 수 있는 패턴이 무수히 많아서 관심을 끈 게임이기도 하며, 컴퓨터 과학에서도 다루고 있는 게임이다.
#
# ----- 규칙 ------
#
# 다음 세대로 넘어갈 때 세포들의 생사가 결정되는데, 인접한 8개의 칸을 기준으로 하며 그 기준은 다음과 같다.
#
# 어떤 칸과 인접한 8칸 중 정확히 3칸에 세포가 살아 있다면 해당 칸의 세포는 그 다음 세대에 살 수 있다. (계속 살아 있거나 죽은 상태에서 살아난다.)
#
# 어떤 칸과 인접한 8칸 중 정확히 2칸에 세포가 살아 있다면 해당 칸의 세포는 살아 있는 상태 혹은 죽은 상태를 계속 유지한다.
#
# 그 이외의 경우[1] 해당 칸의 세포는 다음 세대에 고립돼 죽거나 혹은 주위가 너무 복잡해져서 죽는다. (계속 죽어 있거나 이미 살아 있는 상태라면 죽는다.)
#
# 우리의 목표는 다음과 같다.
#
# 1.총 격자의 크기 n x n 에서 n 을 입력 받는다.
#
# 2.살아있는 세포는 1, 죽은세포는 0으로 표시한다.
#
# 3.초기값(처음에 살아있는 세포의 위치)를 (x,y) 형태로 입력받는다. 이때 특정 숫자 혹은 숫자쌍이나 단어를 입력할때까지 계속 입력받는다.(입력종료) (또는 파일로 불러와도 된다.)
#
# 3.시행횟수(세대 수)를 입력하고 n세대가 지난 후의 결과를 n*n행렬이나 배열 형태로 반환한다.

import numpy as np
import random

def summ_around(row,col,board):
    ans=0
    moving = [[-1,-1],[0,-1],[1,-1], # 왼쪽열 세로로 3개
              [-1,0],[1,0], # 해당열 위아래 2개
              [-1,1],[0,1],[1,1]] # 오른쪽열 세로로 3개
    for step in moving:
        t1 = row +step[0]
        t2 = col +step[1]
        if t1<0 or t2<0 or t1>= board.shape[0] or t2>= board.shape[1]:
            continue
        ans += board[t1,t2]
    return(ans)

def solution(n):
    copy = board.copy()
    for _ in range(n):
        for i in range(n):
            for j in range(n):
                t1=summ_around(i,j,copy) # 근처 8개의 합을 구하기
                if t1 ==3:
                    copy[i,j]=1
                elif t1==2:
                    continue
                else:
                    copy[i,j]=0
    return(copy)

print('n을 입력하세요')
k = input()
n= int(k)
board = np.zeros(n*n).reshape([n,n])
while True:
    print('x좌표값을 입력하세요');x= int(input())
    print('y좌표값을 입력하세요');y= int(input())
    if x<0 or y<0 or x>= board.shape[0] or y>= board.shape[1]:
        break
    board[x,y]=1
solution(n)