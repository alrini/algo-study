from collections import deque

def solution(maps):
    a,b = len(maps), len(maps[0])
    visited = [[0]*b for _ in range(a)]

    answer = []

    for i in range(a):
        for j in range(b):
            if maps[i][j] == "X" or visited[i][j]:
                continue

            queue = deque()
            queue.append((i,j))
            f_day = int(maps[i][j])
            visited[i][j]=1
            while queue:
                x,y = queue.popleft()
                for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx = x+dx
                    ny = y+dy

                    if 0<=nx<a and 0<=ny<b and not visited[nx][ny] and maps[nx][ny]!="X":
                        queue.append((nx,ny))
                        visited[nx][ny]=1
                        f_day += int(maps[nx][ny])
            answer.append(f_day)

    if not answer:
        answer.append(-1)
    else:
        answer.sort()

        return answer