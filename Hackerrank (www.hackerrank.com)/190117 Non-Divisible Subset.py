# Question Link : https://www.hackerrank.com/challenges/non-divisible-subset/problem

from collections import Counter, defaultdict


def nonDivisibleSubset(k, S):
    S = list(map(lambda x : x % k, S))
    dic = defaultdict(lambda : 0, Counter(S)) # This size is always less than k( < 100).
    for i in range(k//2 + 1):
        if i == k/2:
            if dic[i] > 0 :
                dic[i] = 1 # it should not be more than 1
        elif i == 0:
            if dic[0] > 0:
                dic[0] = 1  # it should not be more than 1
        elif dic[i] > dic[k-i]:
            dic[k-i] = 0
        else:
            dic[i] = 0
    result = 0
    for key in dic.keys():
        result += dic[key]
    return result

# Method to Solve : Hash
# Time Complexity : O(n)
# Space Complexity : O(n)

# Restraint : 0 <= n <= 100