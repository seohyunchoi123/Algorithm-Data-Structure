import sys

n = int(sys.stdin.readline())
queue=[]
for _ in range(n):
    t = sys.stdin.readline().split()
    if t[0]=='push':
        queue += t[1] # 이게 어떻게 되는거지 ??? 와 졸라 신기하네
    elif t[0]=='pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif t[0]=='size':
        print(len(queue))
    elif t[0]=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif t[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif t[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        pass

## 아니 왜 공백이 하나 생겨서 나오냐 ...........ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
## 공백은 문제가 아니네 그럼 뭐가 문제야 ? 내 코드가 밑에 정답 코드랑 다른점이 도데체 뭐지?
# from sys import stdin
# qu=[]
# for _ in range(int(stdin.readline())):
#     arr = stdin.readline().split()
#     if arr[0] == 'push':
#         qu.append(arr[1])
#     elif arr[0] == 'pop':
#         if qu: print(qu.pop(0))
#         else: print(-1)
#     elif arr[0] == 'size':
#         print(len(qu))
#     elif arr[0] == 'empty':
#         print(1-int(bool(qu)))
#     elif arr[0] == 'front':
#         if qu: print(qu[0])
#         else: print(-1)
#     elif arr[0] == 'back':
#         if qu: print(qu[-1])
#         else: print(-1)
#     else:
#         pass
