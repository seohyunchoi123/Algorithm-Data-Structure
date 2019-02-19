# Question Link: https://www.hackerrank.com/challenges/almost-sorted/problem


def almostSorted(arr):
    sorted_arr = sorted(arr)
    wrong_idx = []
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            wrong_idx.append(i)
    if len(wrong_idx) == 2: # case of swap
        if arr[wrong_idx[1]] == sorted_arr[wrong_idx[0]] and arr[wrong_idx[0]] == sorted_arr[wrong_idx[1]]:
            print('yes')
            print('swap %d %d' %(wrong_idx[0]+1, wrong_idx[1]+1))
    else: # case of reverse
        sub_arr = arr[wrong_idx[0]:wrong_idx[-1]+1]
        sub_sorted_arr_reversed = sorted_arr[wrong_idx[0]:wrong_idx[-1]+1][::-1]
        for i in range(len(sub_arr)):
            if sub_arr[i] != sub_sorted_arr_reversed[i]:
                print('no')
                return
        print('yes')
        print('reverse %d %d'%(wrong_idx[0]+1, wrong_idx[-1]+1))

# Time Complexity: O(NlogN)
# Space Complexity: O(N)
