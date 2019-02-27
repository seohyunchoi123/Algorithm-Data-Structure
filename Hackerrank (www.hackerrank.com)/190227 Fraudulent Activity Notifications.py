# Question Link: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

def Counting_Sort(List):
    board = [0] * 201
    for n in List:
        board[n] += 1
    for i in range(200):
        board[i + 1] = board[i] + board[i + 1]
    answer = [0] * len(List)
    for n in List:
        answer[board[n] - 1] = n
        board[n] -= 1
    return answer


def binary_tree_add(n, List):
    start = 0
    end = len(List) - 1
    while True:
        idx = (start + end)//2
        if idx == start:
            break
        if List[idx] > n:
            end = idx
        elif List[idx] <= n:
            start = idx
    if n > List[idx] >= 1:
        List.insert(idx + 1, n)
    else:
        List.insert(idx, n)
    return List

def binary_tree_remove(n, List):
    start = 0
    end = len(List) - 1
    while True:
        idx = (start + end)//2
        if List[idx] == n:
            break
        if idx == start:
            idx += 1
            break
        if List[idx] > n:
            end = idx
        elif List[idx] <= n:
            start = idx
    List.pop(idx)
    return List


def activityNotifications(expenditure, d):
    answer = 0
    n = len(expenditure)
    sub_list = Counting_Sort(expenditure[:d])
    for i in range(d, n):
        if i != d:
            sub_list = binary_tree_add(expenditure[i - 1], sub_list)
            sub_list = binary_tree_remove(expenditure[i - d - 1], sub_list)
        if d % 2 == 1:
            median = sub_list[d//2]
        else:
            median = sum(sub_list[d//2 - 1 : d//2 + 1])/2
        if expenditure[i] >= 2 * median:
            answer += 1
    return answer

# Method to Solve: Counting Sort, Binary Search
# Time Complexity: O(n)
# Space Complexity: O(n)