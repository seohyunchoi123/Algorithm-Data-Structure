# The member states of the UN are planning to send  people to the moon. They want them to be from different countries. You will be given a list of pairs of astronaut ID's. Each pair is made of astronauts from the same country. Determine how many pairs of astronauts from different countries they can choose from.
#
# For example, we have the following data on 2 pairs of astronauts, and 4 astronauts total, numbered  through .
#
# 1   2
# 2   3
# Astronauts by country are  and . There are  pairs to choose from:  and .
#
# Function Description
#
# Complete the journeyToMoon function in the editor below. It should return an integer that represents the number of valid pairs that can be formed.
#
# journeyToMoon has the following parameter(s):
#
# n: an integer that denotes the number of astronauts
# astronaut: a 2D array where each element  is a  element integer array that represents the ID's of two astronauts from the same country
# Input Format
#
# The first line contains two integers  and , the number of astronauts and the number of pairs.
# Each of the next  lines contains  space-separated integers denoting astronaut ID's of two who share the same nationality.

# An integer that denotes the number of ways to choose a pair of astronauts from different coutries.
#
# Sample Input 0
# 5 3
# 0 1
# 2 3
# 0 4

# Sample Output 0
# 6


from collections import defaultdict

def dfs(n, astronaut):
    graph = defaultdict(list)
    for edge in astronaut:
        i, j = edge
        graph[i].append(j)
        graph[j].append(i)
    visited = [0] * n
    unvisited = set(range(n))
    results = []
    keys = graph.keys()
    for _ in range(len(keys)): # Finding how many groups there are
        if not set(keys).intersection(unvisited): # No more connected countries to visit
            break
        now = list(set(keys).intersection(unvisited))[0]
        stack = []
        n_visit = 0
        while True: # Finding how many people are connected in each group
            visited[now] = 1
            unvisited = unvisited - {now}
            n_visit += 1
            for candidate in graph[now]:
                if visited[candidate] == 0 and candidate not in stack:
                    stack.append(candidate)
            if not stack:
                results.append(n_visit)
                break
            else:
                now = stack.pop()
    results += [1] * (n-len(graph.keys())) # Filling 1 for unconnected people
    return results
    # results is a list of the number of people connected in each group, or the number of people of each country


def journeyToMoon(n, astronaut):
    results = dfs(n, astronaut)
    answer = 0
    prev_sum = sum(results) # Applying Dynamic Programming for lessening time complexity so you don't need to sum up all the elements in the list for 100,000 times
    for i in range(len(results) - 1):
        answer += results[i] * (prev_sum - results[i])
        prev_sum -= results[i]
    return int(answer)


np = input().split()
n = int(np[0])
p = int(np[1])
astronaut = []
for _ in range(p):
    astronaut.append(list(map(int, input().rstrip().split())))

result = journeyToMoon(n, astronaut)
print(result)

# Method to solve : DFS
# Time Complexity : O(V + E)
# Space Complexity : O(V+ E)
