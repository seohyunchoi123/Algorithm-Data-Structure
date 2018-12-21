# 모든 짝수번째 숫자를 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.) 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.
# #
# # Example: a1b2cde3~g45hi6 → abcde~g4hi6

# 답안
s = list(char)
for i in range(1, len(s), 2):
    if s[i].isdigit() : s[i] = "*"
"".join(s) # character는 인덱싱 수정이 안되니깐 리스트로 바꾼후 나중에 다시 합침 


