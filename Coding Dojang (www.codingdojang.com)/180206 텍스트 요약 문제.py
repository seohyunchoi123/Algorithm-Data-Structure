#
# 문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.
#
# 입력 예시: aaabbcccccca
#
# 출력 예시: a3b2c6a1



char = input()
key = [char[0]]
resul t= ""
for i in range(1, len(char)) :

    if char[i] == key[0] :
        key.append(char[i])
    elif char[i] != key[0] :
        result = result + str(key[0 ] +str(len(key)))
        key = [char[i]]
    if i+ 1 == len(char):
        result = result + str(key[0] + str(len(key)))
print(result)