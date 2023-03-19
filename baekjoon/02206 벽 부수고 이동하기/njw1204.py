from collections import deque

n, m = map(int, input().split())
field = []

for i in range(n):
    field.append(input())

q = deque()
visited = [[[0]*2 for j in range(m)] for i in range(n)]

q.append([0, 0, 0])
visited[0][0][0] = 1

while q:
    node = q.popleft()

    if [node[0], node[1]] == [n - 1, m - 1]:
        print(visited[node[0]][node[1]][node[2]])
        exit(0)

    for dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni, nj, nk = node[0] + dx[0], node[1] + dx[1], node[2]

        if not (0 <= ni < n) or not (0 <= nj < m):
            continue

        if field[ni][nj] == "1":
            if node[2] == 1:
                continue

            nk = 1

        if visited[ni][nj][nk]:
            continue

        q.append([ni, nj, nk])
        visited[ni][nj][nk] = visited[node[0]][node[1]][node[2]] + 1

print(-1)
