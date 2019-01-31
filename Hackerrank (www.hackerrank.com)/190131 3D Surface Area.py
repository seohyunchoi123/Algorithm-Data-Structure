# Question Link : https://www.hackerrank.com/challenges/3d-surface-area/problem

def surfaceArea(A, H, W):
    n_total = 0
    conflicted_up_down = 0
    conflicted_sides = 0

    for i in range(H):
        for j in range(W):
            n_total += A[i][j]
            conflicted_up_down += (A[i][j] - 1)
            if not i == H - 1:
                conflicted_sides += min(A[i][j], A[i + 1][j])
            if not j == W - 1:
                conflicted_sides += min(A[i][j], A[i][j + 1])

    return 6 * n_total - 2 * conflicted_sides - 2 * conflicted_up_down


# Time Complexity : O(n)
# Space Complexity : O(n)
# Limitation : 1 <= n <= 10,000


