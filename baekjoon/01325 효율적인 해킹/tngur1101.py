from collections import deque

n,m = map(int, input().split())

com_map = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
answer = []
maxCnt = 1
for _ in range(m):
    a,b = map(int, input().split())
    com_map[b].append(a)

def bfs(start_point):
    queue = deque()
    visited[start_point] = True
    cnt = 1
    while queue:
        node = queue.popleft()
        for next_node in com_map[node]:
            if visited[next_node]:
                continue
            else:
                visited[next_node] = True
                cnt += 1
                queue.append(next_node)

    return cnt

# answer에 넣어줘야할 것 고려해야할 것
# 1. bfs한 값이 maxCnt보다 클 때 기존 answer에 append해 놓은거 지워놓고 다시 append하면서 갱신
# 2. bfs한 값이 maxCnt와 같을 때는 append만
for i in range(1,n+1):
    val = bfs(i)
    if val > maxCnt:
        maxCnt = val
        answer.clear()
        answer.append(i)
    elif val == maxCnt:
        answer.append(i)

print(" ".join(map(str, answer)))