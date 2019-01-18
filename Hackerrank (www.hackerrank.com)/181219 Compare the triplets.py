# Question Link : https://www.hackerrank.com/challenges/compare-the-triplets/problem

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.

def compareTriplets(a, b):
    alice =0
    bob =0
    for i in range(3):
        if a[i] > b[i]:
            alice +=1
        elif a[i] < b[i]:
            bob +=1
        else:
            pass
    return [alice, bob]

# Time Complexity : O(N)
# Space Complexity : O(N)

