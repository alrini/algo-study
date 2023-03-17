from collections import deque

n,m,k = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(posx,posy):
    global min_cnt
    queue = deque()
    queue.append((posx,posy))
    field[posx][posy] = 1
    cnt = 1

    while queue:
        pos = queue.popleft()
        for i in range(4):
            x = pos[0] + dx[i]
            y = pos[1] + dy[i]
            if 0<=x<n and 0<=y<n and not field[x][y]:
                field[x][y]=1
                cnt += 1
                queue.append((x,y))

    if cnt%k == 0:
        min_cnt -= cnt//k
    else:
        min_cnt -= cnt//k+1

min_cnt = m

for i in range(n):
    for j in range(n):
        if not field[i][j]:
            bfs(i,j)

if min_cnt < 0 or m == min_cnt:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
    print(min_cnt)