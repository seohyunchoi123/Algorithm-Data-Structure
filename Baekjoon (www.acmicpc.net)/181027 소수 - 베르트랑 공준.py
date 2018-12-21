m=123456*2
board = list(range(m + 1))
for i in range(2, m + 1):
    for j in range(2, m + 1):  # 왜 2부터 시작하기를 없애면 답이 게속 0이나오지 ? 당연하지. i의 모든 숫자들이 다 -1로 변하니깐
        t = i * j
        if t > m:
            break
        board[t] = -1  # 소수가 아닌 숫자들에 -1을 메김
board[0]=-1
board[1]=-1
# print(board)
# print(board[:10])
result_2 = []
while True:
    n = int(input())
    if n == 0:
        break
    result = 0
    for t in board[(n+1):(2*n+1)]:
        if t != -1:
            result += 1
    result_2.append(result)

for t in result_2:
    print(t)
