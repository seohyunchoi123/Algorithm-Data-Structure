# Question Link : https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    w = list(w)
    possible = False
    for i in reversed(range(len(w)-1)): # 뒤에서 3번째까지 유지하면서 ~ 뒤에서 N번째까지 유지하면서
        changeable = w[i:]
        sorted_changeable = sorted(changeable)
        for j in range(len(sorted_changeable)):
            if sorted_changeable[j] > changeable[0]: # if it's possible to make a one-level higher number
                possible = True
                changeable.remove(sorted_changeable[j])
                corrected_list = [sorted_changeable[j]] + sorted(changeable) # changing it into one-level higher number
                break
        if possible:
            break
    if possible :
        return "".join(w[:i] + corrected_list)
    else:
        return 'no answer'

# Method to Solve : Sorting
# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Restraint : 1 <= n <= 100


print(biggerIsGreater('a'))



