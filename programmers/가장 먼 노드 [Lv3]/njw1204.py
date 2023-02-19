from collections import deque

def solution(n, edge):
    links = [list() for i in range(n + 1)]

    for a, b in edge:
        links[a].append(b)
        links[b].append(a)

    q = deque()
    visited = [0]*(n + 1)

    q.append(1)
    visited[1] = 1

    while q:
        node = q.popleft()

        for nxt in links[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = visited[node] + 1

    max_dist = max(visited)
    return len([i for i in visited if i == max_dist])