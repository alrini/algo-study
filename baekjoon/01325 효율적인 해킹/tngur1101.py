import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

com_map = [[] for _ in range(n+1)]
answer = []
maxCnt = 1
for _ in range(m):
    a,b = map(int, input().split())
    com_map[b].append(a)

def bfs(start_point):
    queue = deque([start_point])
    visited = [False] * (n+1)
    visited[start_point] = True
    cnt = 1
    while queue:
        node = queue.popleft()
        for next_node in com_map[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                cnt +=1

    return cnt


for i in range(1,n+1):
	cnt = bfs(i)
	if cnt > maxCnt:
		maxCnt = cnt
		answer.clear()
		answer.append(i)
	elif cnt == maxCnt:
		answer.append(i)

print(" ".join(map(str, answer)))
