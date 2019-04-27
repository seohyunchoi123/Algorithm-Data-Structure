def get_winner(s):
    s1, s2 = s
    global enemy_record
    if s1 == s2:
        return None
    else:
        if set(s) == {'P', 'R'}:
            return 'P'
        elif set(s) == {'R', 'S'}:
            return 'R'
        elif set(s) == {'P', 'S'}:
            return 'S'
        else:
            print(s)
            enemy_record.append(list(set(s) - {'ME'})[0])
            return 'ME'

def solution(n, a, s):
    s = list(s)
    s.insert(a, 'ME')
    global enemy_record
    while True:
        next = []
        for i in range(len(s)//2):
            winner = get_winner(s[2*i : 2*i + 2])
            if winner :
                next.append(winner)
        if len(s)%2 == 1:
            next.append(s[-1])
        s = next.copy()

        if next:
           print(next)

        if len(next) == 1:
            break

    print(enemy_record)
    result = 0
    for i in range(len(enemy_record)-1):
        if enemy_record[i] != enemy_record[i+1]:
            result += 1
    return result

enemy_record = []
n, a, s = 43, 32, 'PSPPSPRSPSPSPPSRSPRSRPPPPRSSSSRPSPRRSSPSPP'
print(solution(n,a,s))


