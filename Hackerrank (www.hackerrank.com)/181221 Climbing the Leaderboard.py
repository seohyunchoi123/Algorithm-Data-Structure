# Question Link : https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=internal-search

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = list(sorted(set(scores),reverse=True))
    total_result=[]
    for alice_score in alice:
        # binary search !
        start =0
        end=len(scores)-1
        prev=-1
        while True:
            idx = int((start+end)/2)
            if alice_score >= scores[0]:
                total_result.append(1)
                break
            elif alice_score == scores[-1]:
                total_result.append(len(scores))
                break
            elif alice_score < scores[-1]:
                total_result.append(len(scores)+1)
                break

            if alice_score > scores[idx]:
                end=idx
            elif alice_score < scores[idx]:
                start=idx
            else:
                total_result.append(idx+1)
                break
            if idx==prev: # break condition
                total_result.append(idx+2)
                break
            prev=idx
    return total_result

# Method To Solve : Binary Search Tree
# Time Complexity : O(log N)
# Space Complexity ; O(N)

