# 친화수란 a와 b라는 서로 다른 두 자연수가 있을 때, a의 자신을 제외한 약수를 모두 더하면 b가 되고,
# b의 자신을 제외한 약수를 모두 더하면 a가 되는 두 수의 쌍을 말한다.
# 예로 220, 284을 들면 220의 자신을 제외한 약수는 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110이고, 이를 모두 더하면 284이다.
# 또한 284의 자신을 제외한 약수는 1, 2, 4, 71, 142이고, 이를 모두 더하면 220이 되므로 220과 284는 친화수이다.
#
# 자연수 A를 입력받았을 때, A 이하의 친화수의 쌍의 개수를 출력하는 프로그램을 만들어라.

def ans (A):
    result=[]
    for num in range(1, A):
        if sum(yaksoo(num)) == A and sum(yaksoo(A)) == num:
            result.append(num)
    return(len(result))


print(ans(2924))