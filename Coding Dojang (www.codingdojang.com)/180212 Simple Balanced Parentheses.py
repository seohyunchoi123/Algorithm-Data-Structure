# 아래는 괄호를 이용한 연산식이다.
#
# (5+6)∗(7+8)/(4+3) 우리는 여는 괄호가 있으면 닫는 괄호가 반드시 있어야 한다는 것을 잘 알고 있다.
#
# 다음은 정상적인(balanced) 괄호 사용의 예이다.
#
# (()()()()) (((()))) (()((())())) 다음은 비정상적인(not balanced) 괄호 사용의 예이다.
#
# ((((((()) ())) (()()(() (()))( ())(() 괄호의 사용이 잘 되었는지 잘못 되었는지 판별 해 주는 프로그램을 작성하시오.

def is_balanced (st):
    cnt = 0
    for i in st :
        if i =="(" : cnt+=1
        elif i ==")" : cnt-=1
        if cnt <0: return False
    if cnt !=0: return False
    else: return True
print(is_balanced ("((((((())"))

print(is_balanced("(()((())()))"))