# import sys
# n=int(input())
#
# if n<10:
#     n = n*10
# original_n = n
# idx=0
# while True:
#     a = n//10
#     b = n%10
#     ans = a+b
#     n= b*10 + ans%10
#     idx+=1
#     if n == original_n:
#         break
# print(idx)


print('3'[-1]) # 이려면 3 뱉긴하는데 ..
# 밑에 방법은 왜 틀렸을까?
import sys
n=int(sys.stdin.readline())

if n<10:
    n = int(str(n)+'0')
original_n = n
idx=0
while True:
    ans = 0
    for t in map(int, list(str(n))):
        ans +=t
    n= int(str(n)[1] + str(ans)[-1]) # 이러면 n이 3이 됐을떄 인덱스 오류가 뜰수밖에없다. 오키오키 !!
    idx+=1
    if n == original_n:
        break
print(idx)