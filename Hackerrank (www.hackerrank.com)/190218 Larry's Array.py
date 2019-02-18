# Question Link: https://www.hackerrank.com/challenges/larrys-array/problem

def rotate(arr):
    return [arr[2]] + arr[:2]

def larrysArray(arr):
    for i in reversed(range(len(arr)-2)):
        for j in range(i+1):
            while arr[j+2] != max(arr[j:j+3]):
                arr[j:j+3] = rotate(arr[j:j+3])
    if arr[0] <= arr[1] and arr[1] <= arr[2]:
        return 'YES'
    else:
        return 'NO'

# Time Complexity : O(n^2)
# Space Complexity : O(n)
