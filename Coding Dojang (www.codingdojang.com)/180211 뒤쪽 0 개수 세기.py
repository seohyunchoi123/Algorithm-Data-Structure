# N!의 정의는 다음과 같습니다.
#
# N! = 1 * 2 * 3 * 4 ... N
# 이때 N!를 정수로 변환 해 뒤에서 부터 연속되는 0의 갯수를 구하세요.
#
# 예) f(12) -> 2 # 12!은 479001600 f(25) -> 6 # 25!은 15511210043330985984000000
#
# 출처: codewars

def hi(n):
    def fac(n) :
        if n==1 : return 1
        return n*fac(n-1)
    a = str(fac(n))
    b = list(a)
    b.reverse()
    for i in range(len(b)):
        if b[i] !='0' : return(i)
print(hi(100))