import sys

arr = sys.stdin.readline()
stack=[]
small=0
big=0
is_possible=1
for t in arr:
    if t =='(' :
        small+=1
        stack.append(t)
    elif t=='[':
        big+=1
        stack.append(t)
    elif t ==')' :
        small-=1
        if big < 0 or small < 0:
            is_possible = 0
            break

        summ=0
        while True:
            if stack[-1] !='(':
                if stack[-1]=='[': # 대괄호는 오류이므로 0 반환토록
                    is_possible = 0
                    break
                summ+=stack[-1]
                stack.pop()
            else:
                if summ==0: # 괄호가 열렸다가 바로 닫힌 경우
                    summ=1
                stack.pop()
                stack.append(2*summ)
                break

    elif t ==']':
        big-=1
        if big < 0 or small < 0:
            is_possible = 0
            break

        summ = 0
        while True:
            if stack[-1] != '[':
                if stack[-1]=='(': # 소괄호는 오류이므로 0 반환토록
                    is_possible = 0
                    break
                summ += stack[-1]
                stack.pop()
            else:
                if stack[-1]=='(':
                    is_possible = 0
                    break

                if summ==0: # 괄호가 열렸다가 바로 닫힌 경우
                    summ=1
                stack.pop()
                stack.append(3 * summ)
                break

if big!=0 or small!=0:
    is_possible=0

if is_possible==1:
    print(sum(stack))
else:
    print(0)



# a = [1,2,3]
# print(sum(a))
# print(sum([1,2,3]))



# 방법 1 실패
# formula=[]
# small=0
# big=0
# is_possible=1
# for t in arr:
#     if t=='(':
#         small+=1
#         formula.append('2*(')
#     elif t ==')':
#         small-=1
#         formula.append('1)')
#     elif t=='[':
#         big+=1
#         formula.append('3*(')
#     elif t==']':
#         big-=1
#         formula.append('1)')
#     if big <0 or small<0:
#         is_possible=0
#
# if small!=0 or big!=0:
#     is_possible=0
#
# if is_possible==1:
#     formula = "".join(formula)
#     formula = formula.replace(')2', ')+2')
#     formula = formula.replace(')3', ')+3')
#     formula = formula.replace(')1', ')*1')
#     print(eval(formula))
# else:
#     print(0)
