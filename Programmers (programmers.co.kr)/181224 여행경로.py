# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
#
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.


## Anlaysis ##
# Sorting candidates, explore the map using DFS and return the first right answer !

from collections import defaultdict


def dfs(dic, begin, visited):
    visited.append(begin)
    is_null = True
    for value in dic.values():
        if value:
            is_null = False
    if is_null: # No more any ticket !
        return visited
    for i in range(len(dic[begin])):
        tmp = dic[begin].pop(i)
        ans = dfs(dic, tmp, visited.copy())
        dic[begin].insert(i, tmp)
        if ans: # Return only when they have specific answer !
            return ans


def solution(tickets):
    dic = defaultdict(list) # ticket hash table
    for ticket in tickets:
        dpt, arv = ticket
        dic[dpt].append(arv)
        dic[dpt].sort()
    answer = dfs(dic, 'ICN', [])
    return answer


case_1 = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]
case_2 = [['ICN', 'B'], ['ICN', 'C'], ['B', 'C']]
case_3 = [['ICN', 'B'], ['ICN', 'C'], ['C', 'ICN']]
answer = solution(case_3)
print(answer)

# Method to solve : DFS
# Time Complexity : O(N^2)
# Space Complexity : 0(N^2)