#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    cnt = Counter(x)
    end =0
    result =0
    for i in range(1, max(x)+1):
        if i <= end:
            if cnt[i] > 0 and start >= i-k:
                end = i + k
                continue
            else:
                continue
        if cnt[i]>0:
            start = i
            end = start + k
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# Link: https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
# Time Complexity: O(n)
# Space Complexity: O(n)