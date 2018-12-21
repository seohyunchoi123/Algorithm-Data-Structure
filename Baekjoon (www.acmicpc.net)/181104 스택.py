import sys

# n = int(input())
#
# result = []
# stack = []
# for _ in range(n):
#     t = input().split()
#     if t[0] =='push':
#         stack.append(int(t[1]))
#     elif t[0] =='pop':
#         if len(stack)>0:
#             result.append(stack.pop())
#         else:
#             result.append(-1)
#     elif t[0]=="size":
#         result.append(len(stack))
#     elif t[0]=='empty':
#         if len(stack)>0:
#             result.append(0)
#         else:
#             result.append(1)
#     elif t[0]=="top":
#         if len(stack) >0:
#             result.append(stack[-1])
#         else:
#             result.append(-1)
#
# for t in result:
#     print(t)

t = sys.stdin.readline().strip
print(t)