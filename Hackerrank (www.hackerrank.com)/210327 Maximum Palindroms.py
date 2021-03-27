import math
import os
import random
import re
import sys
from collections import Counter


def answerQuery(l, r, s, factorial, arr):
    l_row = arr[l - 2]
    r_row = arr[r - 1]
    cnt = [0 for _ in range(26)]
    for i in range(26):
        cnt[i] = r_row[i] - l_row[i]

    son = 0
    mom = 1
    multiplier = 0
    for i in range(26):
        if cnt[i] == 0:
            continue
        elif cnt[i] % 2 == 0:
            son += cnt[i] // 2
            mom *= mod[cnt[i] // 2]
        elif cnt[i] % 2 == 1 and cnt[i] > 2:
            son += (cnt[i] - 1) // 2
            mom *= mod[cnt[i] // 2]
            multiplier += 1
        else:
            multiplier += 1

    return factorial[max(son, 1)] * mom * max(multiplier, 1) % m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    q = int(input().strip())
    n = len(s)
    global m
    m = 10 ** 9 + 7

    factorial = [0, 1]  # factorial
    mod = [0, 1]
    for i in range(1, n):
        value = factorial[-1] * (i + 1) % m
        factorial.append(value)
        mod.append(pow(value, m - 2, m))

    arr = [[0 for _ in range(26)] for _ in range(len(s) + 1)]  # count
    for i in range(len(s)):
        for j in range(26):
            if j == ord(s[i]) - 97:
                arr[i][j] = arr[i - 1][j] + 1
            else:
                arr[i][j] = arr[i - 1][j]

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])
        r = int(first_multiple_input[1])
        result = answerQuery(l, r, s, factorial, arr)

        fptr.write(str(result) + '\n')

    fptr.close()

# Link: https://www.hackerrank.com/challenges/maximum-palindromes/problem?isFullScreen=true
# Time Complexity: O(n)