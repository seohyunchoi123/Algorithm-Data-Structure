# Question Link : https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3


def solution(m, n, puddles):
    mat = [[-1 for _ in range(m)] for _ in range(n)]
    for j in range(m): # 가장자리는 가는 방법 모두 1로 채운다
        mat[0][j] = 1
    for i in range(n):
        mat[i][0] = 1
    for j, i in puddles: # 가장자리에 puddle이 있다면 puddle뿐만 아니라 그 뒤쪽으로도 모두 0으로 바꿔준다.
        mat[i - 1][j - 1] = 0
        if j == 1: #
            for k in range(i, n):
                mat[k][0] = 0
        elif i == 1:
            for k in range(j, m):
                mat[0][k] = 0
    # 1차원일 떄
    if m == 1 or n == 1:
        if not puddles:
            return 1
        else:
            return 0
    # 2차원일 때
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 0: # 업뎃하려했던 위치가 puddle일 경우
                continue
            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    return mat[n - 1][m - 1] % 1000000007

# Time Complexity: O(n * m)
# Space Complexiy: O(n * m)