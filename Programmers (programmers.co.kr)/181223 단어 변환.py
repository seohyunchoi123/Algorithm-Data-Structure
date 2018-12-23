# 문제 설명
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
#
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면 hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.
#
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.

def is_connected(word_1, word_2):
    n_different = 0
    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            n_different += 1
    if n_different <= 1:
        return True
    else:
        return False

def bfs(begin, target, words):
    distance = dict(zip(words, [len(words) * len(words)] * len(words)))
    distance[begin] = 0
    queue = [begin]
    visited = []
    while queue:
        begin = queue.pop(0)
        visited.append(begin)
        if begin == target:
            return distance[target]
        for word in words:
            if is_connected(begin, word) and (word not in visited)  \
                    and (word not in queue) and (distance[begin]+1 < distance[word]):
                queue.append(word)
                distance[word] = distance[begin] + 1
    return 0


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer

results = []
ans = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(ans)

# Method to solve : BFS
# Time Complextiy : |V| + |E|
# Space Complextiy : |V| + |E|


# There is another way using DFS finding all the possible ways and choose the shortest route. It's less efficient.
# def dfs(begin, target, words, visited): # Finding all the possible ways and choose the shortest route.
#     visited.append(begin)
#     if begin == target:
#         results.append(len(visited)) # this works ...
#         # results.append(visited) # for debugging
#         print(visited, len(visited)) # this works, but why the right above one doesn't work?
#     else:
#         candidates = []
#         for word in words:
#             if is_connected(begin, word) and word not in visited: # connected & not visited yet
#                 candidates.append(word)
#         if len(candidates) == 0: # no more place to visit newly
#             pass
#         else:
#             for candidate in candidates:
#                 dfs(candidate, target, words, visited)
#                 visited.pop() # to find all possible ways