# 문제 설명
# 앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
# 문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.
#
# 예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.
#
# 제한사항
# 문자열 s의 길이 : 2500 이하의 자연수
# 문자열 s는 알파벳 소문자로만 구성

# 방법 1
def check_odd(s, i):
    n_same = 0
    left = i - 1
    right = i + 1
    while True:
        if left < 0 or right >= len(s) or s[left] != s[right]:
            break
        n_same += 1
        left -= 1
        right += 1
    return 2 * n_same + 1

def check_even(s, i):
    n_same = 0
    left = i
    right = i + 1
    while True:
        if left < 0 or right >= len(s) or s[left] != s[right]:
            break
        n_same += 1
        left -= 1
        right += 1
    return 2 * n_same

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer = max(answer, check_odd(s, i))
        if i != (len(s)-1):
            answer = max(answer, check_even(s, i))
    return answer

# Time Complexity : O(N^2)
# Sapce Complexity : O(N)


# 방법 2
def solution(s):
    answer = 0
    for length in reversed(range(1, len(s)+1)):
        for j in range(len(s) - length + 1):
            sub = s[j:j+length]
            if sub == sub[::-1]:
                return length

# Time Complexity : O(N^2)
# Sapce Complexity : O(N)