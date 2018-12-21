# 일반적으로 괄호가 없는 사칙연산을 계산할 때는 왼쪽에서부터 계산하며, 곱하기와 나누기를 더하기와 빼기보다 먼저 계산한다.
#
# 괄호가 없는 사칙연산 식을 입력받았을 때 오른쪽에서부터, 더하기나 빼기를 곱하기나 나누기보다 먼저 계산한 결과를 리턴하는 코드를 작성하라.
#
# (단, 사칙연산 식은 문자열의 형식으로 입력받는다)

# 시도3 : 종이에 먼저 정리하고 푸니까 바로 풀리자나 ㅡㅡ
import re

k = '2+3*12/15-9/2/2'

def solution(a) :
    tmp1 = re.split('(\D)', a)

    for i in range(len(tmp1)-1):
        if tmp1[i]=="+" or tmp1[i]=="-":
            tmp1[i+1] = str(eval("".join(tmp1[i-1:i+2])))
            tmp1[i-1] = ""
            tmp1[i] = ""
    return(eval("".join(tmp1)))
print(solution(k)) # 풀엇다