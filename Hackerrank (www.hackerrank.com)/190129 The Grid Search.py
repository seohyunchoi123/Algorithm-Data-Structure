# Question Link : https://www.hackerrank.com/challenges/the-grid-search/problem


def check(r, c, row_len_p, col_len_p):
    is_correct = True
    for i in range(row_len_p): # rows
        for j in range(col_len_p): # columns
            if G[r+i][c+j] != P[i][j]:
                return False
    if is_correct:
        return True


def gridSearch(G, P):
    row_len_p = len(P)
    col_len_p = len(P[0])
    row_len_g = len(G)
    col_len_g = len(G[0])
    is_yes = False
    for i in range(row_len_g - row_len_p + 1):
        for j in range(col_len_g - col_len_p + 1):
            if check(i, j, row_len_p, col_len_p):
                return "YES"
    if not is_yes:
        return "NO"

G = [[4,3,2],
     [1,5,6],
     [6,7,1]]

P = [[5,6],
     [7,1]]

print(gridSearch(G, P))

# Time Complextiy : O(n^2)
# Space Complexity : O(n^2)
# limitation : 1 <= n <= 1000