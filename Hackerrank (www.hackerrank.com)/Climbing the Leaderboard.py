# Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:
#
# The player with the highest score is ranked number  on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# For example, the four players on the leaderboard have high scores of , , , and . Those players will have ranks , , , and , respectively. If Alice's scores are ,  and , her rankings after each game are ,  and .
#
# Function Description
#
# Complete the climbingLeaderboard function in the editor below. It should return an integer array where each element represents Alice's rank after the  game.
#
# climbingLeaderboard has the following parameter(s):
#
# scores: an array of integers that represent leaderboard scores
# alice: an array of integers that represent Alice's scores
# Input Format
#
# The first line contains an integer , the number of players on the leaderboard.
# The next line contains  space-separated integers , the leaderboard scores in decreasing order.
# The next line contains an integer, , denoting the number games Alice plays.
# The last line contains  space-separated integers , the game scores.
#

# The existing leaderboard, , is in descending order.
# Alice's scores, , are in ascending order.

# Print  integers. The  integer should indicate Alice's rank after playing the  game.

#!/bin/python3

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

# Time Complexity = O(log N)
# Space Complexity = O(N)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
