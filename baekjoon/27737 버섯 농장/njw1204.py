from collections import deque

n, m, k = map(int, input().split())
field = [[0] * 105 for _ in range(105)]
visited = [[False] * 105 for _ in range(105)]

for i in range(n):
	for j, x in enumerate(map(int, input().split())):
		field[i][j] = x

ans = 0

for i in range(n):
	for j in range(n):
		if visited[i][j] or field[i][j]:
			continue

		q = deque()
		com_size = 1
		q.append([i, j])
		visited[i][j] = True

		while q:
			node = q.popleft()

			for dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
				ni, nj = node[0] + dx[0], node[1] + dx[1]

				if not (0 <= ni < n) or not (0 <= nj < n):
					continue

				if visited[ni][nj] or field[ni][nj]:
					continue

				q.append([ni, nj])
				visited[ni][nj] = True
				com_size += 1

		ans += (com_size + k - 1) // k

if ans > m or ans == 0:
	print("IMPOSSIBLE")
else:
	print("POSSIBLE")
	print(m - ans)
