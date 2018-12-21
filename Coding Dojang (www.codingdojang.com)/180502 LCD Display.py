# LCD Display
# 한 친구가 방금 새 컴퓨터를 샀다. 그 친구가 지금까지 샀던 가장 강력한 컴퓨터는 공학용 전자 계산기였다. 그런데 그 친구는 새 컴퓨터의 모니터보다 공학용 계산기에 있는 LCD 디스플레이가 더 좋다며 크게 실망하고 말았다. 그 친구를 만족시킬 수 있도록 숫자를 LCD 디스플레이 방식으로 출력하는 프로그램을 만들어보자.
#
# 입력
# 입력 파일은 여러 줄로 구성되며 표시될 각각의 숫자마다 한 줄씩 입력된다. 각 줄에는 s와 n이라는 두개의 정수가 들어있으며 n은 출력될 숫자( 0<= n <= 99,999,999 ), s는 숫자를 표시하는 크기( 1<= s < 10 )를 의미한다. 0 이 두 개 입력된 줄이 있으면 입력이 종료되며 그 줄은 처리되지 않는다.
#
# 출력
# 입력 파일에서 지정한 숫자를 수평 방향은 '-' 기호를, 수직 방향은 '|'를 이용해서 LCD 디스플레이 형태로 출력한다. 각 숫자는 정확하게 s+2개의 열, 2s+3개의 행으로 구성된다. 마지막 숫자를 포함한 모든 숫자를 이루는 공백을 스페이스로 채워야 한다. 두 개의 숫자 사이에는 정확하게 한 열의 공백이 있어야 한다.
#
# 각 숫자 다음에는 빈 줄을 한 줄 출력한다. 밑에 있는 출력 예에 각 숫자를 출력하는 방식이 나와있다.

s=2
a='12345'
def my_func(s, a):
    if s == 0 and a == 0:
        return

    a = str(a)
    for ch in a:
        if ch not in ['1', '4']:
            print(' ' + '-' * s + ' ', end=' ')
        else:
            print(' ' * (s + 2), end=' ')
    print('\n')

    # 위
    for _ in range(s):
        for ch in a:
            t = ''
            if ch in ['4', '5', '6', '8', '9', '0']:  # 왼쪽작대기 조건
                t += '|'
            else:
                t += ' '
            t = t + ' ' * s
            if ch not in ['5', '6']:  # 오른쪽작대기 조건
                t += '|'
            else:
                t += ' '
            print(t, end=' ')
        print('\n')

    for ch in a:
        if ch not in ['1', '7', '0']:
            print(' ' + '-' * s + ' ', end=' ')
        else:
            print(' ' * (s + 2), end=' ')
    print('\n')

    # 아래
    for _ in range(s):
        for ch in a:
            t = ''
            if ch in ['2', '6', '8', '0']:  # 왼쪽작대기 조건
                t += '|'
            else:
                t += ' '
            t = t + ' ' * s
            if ch not in ['2']:  # 오른쪽작대기 조건
                t += '|'
            else:
                t += ' '
            print(t, end=' ')
        print('\n')

    for ch in a:
        if ch not in ['1', '4', '7']:
            print(' ' + '-' * s + ' ', end=' ')
        else:
            print(' ' * (s + 2), end=' ')
    print('\n')


def solution(tmp):
    for t in tmp:
        s, a = t.split(' ')
        my_func(int(s), a)
    print('\n')


a = []
while True:
    input_num = input()
    if input_num == '': break
    a.append(input_num)
solution(a)