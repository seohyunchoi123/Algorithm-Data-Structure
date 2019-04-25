# Question Link: https://www.hackerrank.com/challenges/richie-rich/problem


def highestValuePalindrome(s, n, k):
    s = list(s)
    unmatched_idx = [0] * (len(s)//2)
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 -i]:
            unmatched_idx[i] = 1
    n_left_to_change = sum(unmatched_idx)

    if sum(unmatched_idx) > k:
        return "-1"

    for i in range(len(s)//2):
        if s[i] == '9' and s[len(s) -1 -i] == '9':
            continue
        elif s[i] == '9' or s[len(s) -1 -i] == '9':
            cost = 1
        else:
            cost = 2
        # the number of future cases you should change for palindrome
        if unmatched_idx[i] == 1:
            n_left_to_change -= 1
        # if Could I be this luxurious to change this to 9?
        if cost + n_left_to_change <= k:
            k -= cost
            s[i] = '9'
            s[len(s) -1 -i] = '9'
        elif unmatched_idx[i] == 1:
            k -= cost
            value = max(s[i], s[len(s) -1 -i])
            s[i] = value
            s[len(s) -1 -i] = value
        else:
            continue
    if k >= 1 and len(s)%2 ==1:
        s[len(s)//2] = '9'
    return "".join(s)


# Time Complexity: O(N)
# Space Complexity: O(N)