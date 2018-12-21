import sys

n_node, n_line, start = list(map(int, sys.stdin.readline().split()))
graph={}
for _ in range(n_line):
    left, right = list(map(int, sys.stdin.readline().split()))
    if left not in graph.keys():
        graph[left] = [right]
    else:
        graph[left].append(right)

    if right not in graph.keys():
        graph[right] = [left]
    else:
        graph[right].append(left)

def dfs(graph, start):
    visit=[]
    stack=[start]
    while stack:
        tmp = stack.pop()
        if tmp not in visit:
            visit.append(tmp)
        else:
            continue
    stack = stack + sorted(graph[tmp],reverse=True)

    return visit

def bfs(graph, start):
    visit =[]
    queue=[start]
    while queue:
        tmp = queue.pop()
        if tmp not in visit:
            visit.append(tmp)
        else:
            continue
        queue = sorted(graph[tmp],reverse=True) + queue
    return visit

for t in dfs(graph, start):
    print(t, end=' ')
print('')
for t in bfs(graph, start):
    print(t, end=' ')


# t={1:2}
# t={}
# # t[1] = t.get(1,3)
# print(t.get(1,3))
# t.get()
# # t={}
# t['a'] = [1,2,3]
# print(t['a'])
# t['a'].append(4)
# print(t['a'])
#
# t = list(range(10))
# while t: #
#     print(t.pop()) # 맨뒤부터 뽑아내는거 맞는데 ..
#
# print(list(set([4,3,2])))
# print(set([4,3,2]))
# print(list(sorted(set([2,3,4]), reverse=True)))
# print(set([1,2,3]).union(set([2,3,4])))
#
# t = sorted(set([1,3,2]))
# print(type(t))
