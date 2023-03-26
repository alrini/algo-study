from collections import deque
from itertools import combinations

field = []

for i in range(5):
    field.append(input())

ans = 0

for idxs in combinations(range(25), 7):
    points = [[i // 5, i % 5] for i in idxs]
    q = deque()
    visited = [[False] * 5 for i in range(5)]
    conn = 0

    q.append(points[0])
    visited[points[0][0]][points[0][1]] = True
    conn += 1

    while q:
        node = q.popleft()

        for dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = node[0] + dx[0], node[1] + dx[1]

            if [ni, nj] not in points:
                continue

            if visited[ni][nj]:
                continue

            q.append([ni, nj])
            visited[ni][nj] = True
            conn += 1

    if conn != 7:
        continue

    if [field[point[0]][point[1]] for point in points].count("S") >= 4:
        ans += 1

print(ans)
