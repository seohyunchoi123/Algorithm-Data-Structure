# 다음은 233 이란 10진수를 2진수로 변환하는 과정을 나타낸 그림이다.
#
#
#
# 위 그림을 참조하여 라이브러리를 사용하지 말고 10진수를 n진수로 변환하는 프로그램을 작성하시오.. (단, n의 범위는 2 <= n <= 16)
#
# 예)
#
# 2진수로 변환 : 23310 --> 111010012
# 8진수로 변환 : 23310 --> 3518
# 16진수로 변환 : 23310 --> E916


def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


print( convert(233, 2))
print (convert(233, 8))
print (convert(233, 16))