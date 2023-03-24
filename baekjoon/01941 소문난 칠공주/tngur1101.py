from collections import deque

arr = [input() for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
answer = 0

def bfs(si,sj):
    queue = deque()
    vv = [[0]*5 for _ in range(5)]

    queue.append((si,sj))
    vv[si][sj]=1
    cnt = 1

    while queue:
        ci, cj = queue.popleft()
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):  #상하좌우
            nx, ny = ci+dx, cj+dy
            if 0<=nx<5 and 0<=ny<5 and vv[nx][ny]==0 and visited[nx][ny]==1:
                queue.append((nx,ny))
                vv[nx][ny] = 1
                cnt += 1

    return cnt==7

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j]==1:
                return bfs(i,j)

def dfs(n, cnt, scnt):
    global answer

    if cnt>7:
        return 

    if n==25:
        if cnt==7 and scnt>=4:  # 7명 그룹이고, 4명 이상이 다솜파인 경우  
            if check():     # 인접했는지 체크해서 모두 인접시 정답 +1
                answer += 1
        return

    # 포합하는 경우
    visited[n//5][n%5]=1    # 표시
    dfs(n+1, cnt+1, scnt + int(arr[n//5][n%5]=="S"))
    visited[n//5][n%5]=0    #원상복구
    # 포합하지 않는 경우
    dfs(n+1, cnt, scnt)

            

#학생번호(0~24), 포합학생수, 다솜파학생수
dfs(0,0,0)

print(answer)