# 아래가 정석 ! but 이 문제에서는 arr 저장 없이 풀어야함
# n = int(input())
# arr =[]
# max_value=0
# for _ in range(n):
#     t=int(input())
#     arr.append(t)
#     max_value = max(t,max_value)
#
# c = [0]*(max_value+1)
# for i in range(n): # c 형성
#     num = arr[i]
#     c[num]+=1
#
# for i in range(len(c)-1): # c를 누적합으로 바꿔주기
#     c[i+1] = c[i] + c[i+1]
#
# result=[0]*n # 새로운 리스트에 정렬하기 !
# for i in reversed(range(n)):
#     num = arr[i]
#     c[num] -=1
#     idx = c[num]
#     result[idx]=num
#     print(result)
import sys

n = int(input())
max=10000
c=[0]*(max+1)
for _ in range(n): # arr 저장 과정 생략하고 바로 c 만들기
    num = int(sys.stdin.readline()) # input()으로 하면 시간초과난다 !!!
    c[num]+=1

for i in range(max+1):
    for _ in range(c[i]):
        print(i)



