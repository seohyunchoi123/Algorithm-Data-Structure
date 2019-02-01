# Question Link: https://www.hackerrank.com/challenges/absolute-permutation/problem


def absolutePermutation(n, k):
    result = []
    is_used = [0] * n
    prev_idx = -1
    plus_minus_idx = []
    for i in range(n):
        pos = i + 1
        if not plus_minus_idx: # K is the size of cycle!
            plus_minus_idx.append(-1 * prev_idx)
            plus_minus_idx = plus_minus_idx * k
        if not plus_minus_idx: # in case of k = 0
            plus_minus_idx.append(0)
        prev_idx = plus_minus_idx.pop()
        tmp = pos + prev_idx * k # element to add
        if tmp < 1 or tmp > n or is_used[tmp-1] == 1: # In case that an element is beyond the given range, or already appeared
            return[-1]
        result.append(tmp)
        is_used[tmp - 1] = 1 # checkingn that I used this element
    return result


print(absolutePermutation(6, 1))
print(absolutePermutation(3, 0))

# Time Complexity : O(n)
# Space Complexity : O(n)