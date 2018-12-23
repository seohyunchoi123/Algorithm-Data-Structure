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
            if is_connected(begin, word) and (word not in visited)  and (word not in queue) and (distance[begin]+1 < distance[word]):
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