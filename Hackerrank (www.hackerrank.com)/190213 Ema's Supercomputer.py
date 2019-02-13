# Question Link: https://www.hackerrank.com/challenges/two-pluses/problem

def how_many(n, m, grid, r_idx, c_idx):
    ans = 1
    while True:
        is_pass = True
        if r_idx + ans >= n or grid[r_idx + ans][c_idx] == 'B':
            is_pass = False
        if r_idx - ans < 0 or grid[r_idx - ans][c_idx] == 'B':
            is_pass = False
        if c_idx + ans >= m or grid[r_idx][c_idx + ans] == 'B':
            is_pass = False
        if c_idx - ans < 0 or grid[r_idx][c_idx - ans] == 'B':
            is_pass = False

        if is_pass:
            ans += 1
        else:
            return ans - 1

def is_conflicted(cand_1, cand_2):
    if cand_1[0] == cand_2[0]:  # on the same row
        if abs(cand_1[1] - cand_2[1]) > (cand_1[2] + cand_2[2]):  # if not conflicted!
            return False
        else:
            return True
    elif cand_1[1] == cand_2[1]:  # on the same column
        if abs(cand_1[0] - cand_2[0]) > (cand_1[2] + cand_2[2]):
            return False
        else:
            return True
    else:  # on different row and column
        row_diff = abs(cand_1[0] - cand_2[0])
        col_diff = abs(cand_1[1] - cand_2[1])
        if cand_1[2] >= row_diff and cand_2[2] >= col_diff:  # if conflicted
            return True
        elif cand_1[2] >= col_diff and cand_2[2] >= row_diff:  # if conflicted
            return True
        else:
            return False


def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    cands = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G':
                cands.append([i, j, how_many(n, m, grid, i, j)])
    results = []
    for cand_1 in cands:
        for cand_2 in cands:
            if cand_1[0] == cand_2[0] and cand_1[1] == cand_2[1]:
                continue
            if is_conflicted(cand_1, cand_2):
                cand_1_copied = cand_1.copy() # if not copied, the original elements would be changed. WARNING!
                cand_2_copied = cand_2.copy()
                while is_conflicted(cand_1_copied, cand_2_copied): # POINT!! if two are conflicted, you should check other results after lessening their lengths until they aren't conflicted anymore.
                    if cand_1_copied[2] >= cand_2_copied[2]:
                        cand_1_copied[2] -= 1
                    else:
                        cand_2_copied[2] -= 1
                results.append((1 + 4 * cand_1_copied[2]) * (1 + 4 * cand_2_copied[2]))
            else:
                results.append((1 + 4 * cand_1[2]) * (1 + 4 * cand_2[2]))
    return max(results)

# Time Complexity : O(n^2)
# Time Complexity : O(n^2)
# Restrict : 1 <= n <= 225