# Question Link: https://www.hackerrank.com/challenges/magic-square-forming/problem

def formingMagicSquare(s):
    magics = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
             [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],
             [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]

    cand = []
    for magic in magics:
        summ = 0
        for i in range(3):
            for j in range(3):
                summ += abs(s[i][j] - magic[3*i + j])
        cand.append(summ)
    return min(cand)

# Time Complexiy: O(n^2)
# Space Compexity: O(n^2)
