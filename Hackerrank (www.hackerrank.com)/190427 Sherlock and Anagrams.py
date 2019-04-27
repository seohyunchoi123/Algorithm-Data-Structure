# Question Link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

def is_ana(s1, s2):
    if len(s1) != len(s2):
        return False
    result = True
    for ch1, ch2 in zip(sorted(s1), sorted(s2)):
        if ch1 != ch2:
            result = False
    return result


def sherlockAndAnagrams(s):
    result = 0
    for length in range(1, len(s)):
        for i in range(len(s) - length):
            s1 = s[i:i+length]
            for j in range(i + 1, len(s)):
                s2 = s[j:j+length]
                if is_ana(s1,s2):
                    result += 1
                    print(s1,s2)
    return result

s = 'ifailuhkqq'
print(sherlockAndAnagrams(s))