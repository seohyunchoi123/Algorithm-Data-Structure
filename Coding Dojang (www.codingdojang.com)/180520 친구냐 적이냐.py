# 친구냐 적이냐?
# 여러분은 이웃한 나라인 A국으로 스파이를 파견했다. A국의 국회는 야당과 여당의 2당 체제인데, A국의 정치인들은 직선적이고 한번 뜻을 세우면 굽히지 않는 강직한 성격을 가지고 있다. 따라서 A국의 정치인들은 다음과 같은 원칙에 따라 편을 가른다.
#
# 나의 친구의 친구는 나의 친구이다. 나의 친구의 적은 나의 적이다. 나의 적의 친구는 나의 적이다. 나의 적의 적은 나의 친구이다. A국에 파견된 첩보원은 자신이 알아낸 A국 정치인들 사이의 인간관계를 지속적으로 보고하고 있다.
#
# 그런데 당신은 요즘 이 첩보원이 적에게 포섭되어 배신한 것이 아닌지 의심하고 있다. 만일 그가 배신하여 잘못된 정보를 알려준다면 대 A국 전략을 수립하는 데에 어려움이 생길 것이다.
#
# 정치인인 동시에 유능한 프로그래머이자 장래가 촉망받는 치킨업 후계자인 여러분은 스파이가 거짓말을 하고 있는지를 검사해 보려고 한다.
#
# 입력 형식 첫 줄에 A국 정치인의 수 N(<=100000), 처리할 명령의 수 M(<=1000000)이 주어진다.
#
# 이후 M개의 줄에 대해서 다음 형식의 입력이 들어온다.
#
# a b x : 첩보원이 a와 b가 친구 또는 적이라는 보고를 했음을 말한다. x가 'e'이면 두 정치인은 적이고, 'f'이면 두 정치인은 친구이다.
#
# 출력 형식 스파이의 보고 중에서 모순이 발생하는 첫 번째 보고의 번호를 출력한다. 입력의 마지막까지 모순이 발생하지 않았다면 "THE SPY DID NOT BETRAY"를 출력한다.
#
# 입력 예제 3 3 1 2 f 2 3 e 1 3 f
#
# 출력 예제 3 해설) 1과 2는 친구이고 2와 3이 적이므로 1과 3은 서로 적이어야 한다. 입력 예제 5 7 1 2 f 3 4 e 4 5 f 2 4 e 1 3 e 1 4 e 5 3 e
#
# 출력 예제 5

import numpy as np
import pandas as pd

t = input('A국의 정치인수, 처리할 명령수 순으로 입력하시오 ex)3 5 ')
n, m = map(int,  t.split(' '))
info_list=[]
for _ in range(m):
    info = input().split(' ')
    info_list.append(info)

team_1 = ['1']
team_not_1 = ['None'] # 이게 마지막까지 텅 비어있으면 22번째줄에서 오류가남. 뭐라도 넣어주자
for pal in team_1:
    idx=0
    for info in info_list:
        idx +=1
        if pal in info:
        #if info[0] in pal or info[1] in pal:
            if info[2] == 'f':
                team_1.append(np.array(info[:2])[np.array(info[:2]) != np.array(pal)][0])
                info_list.remove(info)
            if info[2] == 'e':
                team_not_1.append(np.array(info[:2])[np.array(info[:2]) != np.array(pal)][0])
                info_list.remove(info)
#        team_1 = list(set(team_1))
#        team_not_1 = list(set(team_not_1))
if any(pd.Series(team_1).isin(pd.Series(team_not_1))):
    print(idx)
    idx =-1
    break
if idx != -1:
    print('He has not betrayed')
else:
    print('He might be spying on you.')