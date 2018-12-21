# 배열 [a, b, c, d]를 입력하면 배열[bcd, acd, abd, abc]를 출력하는 코드를 작성하시오.
#
# (단, 나눗셈 사용 금지)
#
# 입출력되는 배열은 어떤 형식이든 상관없습니다.



def solution(t):
    a,b,c,d = t
    return([b*c*d, a*c*d, a*b*d, a*b*c])

solution([2,6,4,7])

def solution(t):
    ans=[]
    for i in range(len(t)):
        tmp=t.copy()
        tmp.pop(i)
        tmp = [str(num) for num in tmp]
        tmp="*".join(tmp)
        ans.append(eval(tmp))
    return(ans)

print(solution([2,6,4,7]))