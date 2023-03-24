from collections import deque
n, m = map(int, input().split())

map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]     # 3차원으로 생성 0은 벽 부수기 전, 1은 벽 부순 후
dx = [1,0,-1,0]
dy = [0,-1,0,1]
answer = 0

def bfs():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1

    while queue:
        cx, cy, crash = queue.popleft()
        if cx == n-1 and cy == m-1:
            return visited[cx][cy][crash]


        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m: # 맵 영역 안 체크
                if map[nx][ny] == 0 and visited[nx][ny][crash] == 0:    # 다음이 벽이 아니고 방문 안했을 때
                    visited[nx][ny][crash] = visited[cx][cy][crash] +1
                    queue.append((nx, ny, crash))
                if map[nx][ny]==1 and visited[nx][ny][crash] == 0:
                    if crash == 0:  # 벽 아직 안부수었을 때
                        visited[nx][ny][1] = visited[cx][cy][crash] + 1
                        queue.append((nx,ny,1))
                    if crash == 1:  # 이미 벽을 부수었을 때
                        continue
    return -1

answer = bfs()


print(answer)