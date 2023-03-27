from collections import deque

links = [[] for _ in range(10005)]
n, m = map(int, input().split())

for i in range(m):
    a, b = map(int, input().split())
    links[b].append(a)

visited = [0] * 10005
ans = 0
ans_arr = []

for i in range(1, n + 1):
    q = deque()
    q.append(i)
    visited[i] = i
    tans = 1

    while q:
        node = q.popleft()

        for nnode in links[node]:
            if visited[nnode] == i:
                continue

            q.append(nnode)
            visited[nnode] = i
            tans += 1

    if tans > ans:
        ans = tans
        ans_arr = [i]
    elif tans == ans:
        ans_arr.append(i)

print(" ".join(map(str, ans_arr)))
