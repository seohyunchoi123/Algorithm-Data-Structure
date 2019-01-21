# Question Link : https://www.hackerrank.com/challenges/extra-long-factorials/problem

def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n-1)

print(extraLongFactorials(100))

# Mehtod to Solve : Recursion
# Time Complexity : O(n)
# Space Complexity : O(1)