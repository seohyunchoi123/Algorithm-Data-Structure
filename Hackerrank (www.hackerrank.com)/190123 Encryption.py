# Question Link : https://www.hackerrank.com/challenges/encryption/problem

def encryption(s):
    s = s.replace(" ", "")
    minimum = int(len(s)**(1/2))
    length = len(s)
    if minimum * minimum >= length:
        row = minimum
        col = minimum
    elif minimum * (minimum + 1) >= length:
        row = minimum
        col = minimum + 1
    else:
        row = minimum + 1
        col = minimum + 1

    result = []
    for i in range(col):
        string = ''
        for j in range(row):
            if i + col*j >= length:
                continue
            string += s[i + col*j]
        result.append(string)

    return " ".join(result)


s = 'have a nice day'
print(encryption(s))

# Time Complexity : O(n)
# Space Complextiy : O(n)