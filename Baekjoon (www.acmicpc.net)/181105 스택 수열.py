import sys

n = int(sys.stdin.readline())
arr = list(range(1,n+1))
board=[0]*n # 아웃된 숫자들을 체크하기 위한 idx표
idx=0
result=['+']
is_possible=1
for _ in range(n):
    num = int(sys.stdin.readline())
    if num > arr[idx]:
        while board[idx+1] == -1: # 이미 아웃된 숫자를 피해 idx를 옮긴다. 아직 아웃 안된 숫자의 직전에 idx를 갖다놓기 위함임.
            idx += 1
        while True: # 지정한 숫자를 향해 움직인다
            result.append('+')
            idx+=1
            if arr[idx] == num:
                board[idx]=-1
                result.append('-')
                break
    else:
        while board[idx] == -1: # 아직 아웃안된 숫자를 찾아 idx를 옮긴다
            idx -= 1
        if arr[idx] != num: # 아웃되야하는 숫자가 입력된 숫자와 다르면 stack의 원리에 어긋나므로 NO 반환
            is_possible=0
            break
        result.append('-')
        board[idx]=-1

if is_possible==1:
    for t in result:
        print(t)
else:
    print('NO')

