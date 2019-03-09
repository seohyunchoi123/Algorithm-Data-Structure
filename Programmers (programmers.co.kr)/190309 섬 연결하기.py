# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42861
#
# 문제 설명
# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.
#
# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.
#
# 제한사항
#
# 섬의 개수 n은 1 이상 100 이하입니다.
# costs의 길이는 ((n-1) * n) / 2이하입니다.
# 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
# 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
# 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
# 연결할 수 없는 섬은 주어지지 않습니다.
# 입출력 예
#
# n	costs	return
# 4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4

def is_all_connected(n, map):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for cost in map:
        mat[cost[0]][cost[1]] = 1
        mat[cost[1]][cost[0]] = 1
    stack = [0]
    visited = []
    while True:
        start = stack.pop()
        visited.append(start)
        for i in range(len(mat[start])):
            if mat[start][i] == 1 and i not in visited and i not in stack:
                stack.append(i)
        if not stack:
            if len(visited) == n:
                return True
            else:
                return False


def is_two_connected(n, map, a, b):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for cost in map:
        mat[cost[0]][cost[1]] = 1
        mat[cost[1]][cost[0]] = 1
    stack = [a]
    visited = []
    while True:
        start = stack.pop()
        if start == b:
            return True
        visited.append(start)
        for i in range(len(mat[start])):
            if mat[start][i] == 1 and i not in visited and i not in stack:
                stack.append(i)
        if not stack:
            return False


def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x : x[2])
    constructed = []
    for cost in costs:
        if is_two_connected(n, constructed, cost[0], cost[1]): # 이미 이어진 애들을 또 이으려는 거면 continue!
            continue
        constructed.append(cost)
        answer += cost[2]
        if is_all_connected(n, constructed): # 다 이어지면 패스
            return answer

# Method to Solve: Greedy, DFS
# Time Complexity: O(n^2)
# Space Complexity : O(n^2)