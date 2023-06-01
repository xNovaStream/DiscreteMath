from collections import deque


def bfs():
    global graph, coloring
    used = [False] * n
    queue = deque()
    queue.append(0)
    coloring[0] = 0
    while len(queue) != 0:
        v = queue.popleft()
        color = (coloring[v] + 1) % 2
        if not used[v]:
            used[v] = True
            for u in graph[v]:
                if not used[u]:
                    coloring[u] = color
                    queue.append(u)
                elif coloring[u] != color:
                    return False
    return True


n = int(input())
graph = [[] for i in range(n)]
coloring = [-1]*n
for i in range(n):
    for j in map(int, input().split()[:-1]):
        j -= 1
        graph[i].append(j)
        graph[j].append(i)
if bfs():
    print(''.join(map(str, coloring)))
else:
    print(-1)
