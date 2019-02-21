# Question Link: https://www.hackerrank.com/challenges/countingsort4/problem

def countSort(arr):
    ans = [[] for _ in range(100)]
    length = len(arr)
    for i in range(length):
        idx = int(arr[i][0])
        string = arr[i][1]
        if i < length // 2:
            string = '-'
        if not ans[idx]:
            ans[idx].append(string)
        else:
            ans[idx].append(string)
    for ele in ans:
        for sub_ele in ele:
            print(sub_ele, end = ' ')

# Time Complexity : O(n)
# Space Complexity : O(n)