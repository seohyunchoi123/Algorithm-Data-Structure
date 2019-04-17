# Question Link: https://www.hackerrank.com/challenges/lilys-homework/problem


def solution(arr):
    dic = dict(zip(arr, range(len(arr))))
    sorted_arr = sorted(arr)
    n_swap = 0
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            idx_to_swap = dic[sorted_arr[i]]
            dic[arr[idx_to_swap]] = i
            dic[arr[i]] = idx_to_swap
            arr[i], arr[idx_to_swap] = arr[idx_to_swap], arr[i]
            n_swap += 1
            print(arr)
    return n_swap


def lilysHomework(arr):
    a = solution(arr.copy())
    b = solution(arr.copy()[::-1])
    return min(a, b)

# Time Complexity: O(N)
# Space Complexity: O(N)
# Key Technique: Hash