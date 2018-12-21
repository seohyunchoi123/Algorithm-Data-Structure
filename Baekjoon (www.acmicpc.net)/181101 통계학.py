import sys

n = int(input())
arr=[]
board = [0]*8001 # idx - 4000 하면 idx에 해당하는 수임
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    idx = num+4000
    board[idx]+=1

most_freq_num=0 # board에 누적처리해주기전에 최빈값 구하기
max_freq = max(board)
max_idx_list=[]
cnt=0
for i in range(8001):
    if board[i]== max_freq:
        cnt+=1
        max_idx_list.append(i-4000)
if cnt >1 :
    most_freq_num = max_idx_list[1]
else:
    most_freq_num = max_idx_list[0]

for i in range(8000): # board 누적
    board[i+1] += board[i]

new = [0]*n
for t in reversed(arr):
    idx = t+4000
    new_idx = board[idx]
    new[new_idx-1] = t
    board[idx]-=1

print(round(sum(new)/n))
print(new[n//2])
print(most_freq_num)
print(new[-1]-new[0])
