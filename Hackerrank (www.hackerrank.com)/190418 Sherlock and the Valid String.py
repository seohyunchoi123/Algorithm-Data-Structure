# Question Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import defaultdict, Counter


def is_all_same(arr):
    count = [(key, value) for key, value in Counter(arr).items()]
    if len(count) == 1:
        return True
    else:
        return False

def isValid(s):
    dic = defaultdict(lambda : 0)
    for ch in s:
        dic[ch] += 1
    # if all has the same number
    if is_all_same(dic.values()):
        return 'YES'
    # minus 1 for every case
    values = list(dic.values())
    result = 'NO'
    for i in range(len(values)):
        copy = values.copy()
        copy[i] -= 1
        if copy[i] == 0:
            copy.pop(i)

        if is_all_same(copy):
            result = 'YES'
    return result

# Time Complexity: O(n)
# Space COmplextiy: O(n)

