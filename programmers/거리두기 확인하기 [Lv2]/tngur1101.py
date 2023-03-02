#bfs, dfs 문제
from collections import deque

def bfs(arr):
    start = []
    
    for i in range(5):  #시작점이 되는 파티션 찾기
        for j in range(5):
            if arr[i][j] == "P":
                start.append([i,j])
    
    for s in start:
        queue = deque([s])
        distance = [[0]*5 for _ in range(5)]    # 길이
        visited = [[0]*5 for _ in range(5)]
        visited[s[0]][s[1]]=1
        
        while queue:
            x,y = queue.popleft()
            dx = [0,0,-1,1]
            dy = [-1,1,0,0]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0:
                    if arr[nx][ny] == "O":
                        queue.append([nx,ny])
                        visited[nx][ny]=1
                        distance[nx][ny] = distance[x][y]+1
                    if arr[nx][ny] == "P" and distance[x][y]<=1:
                        return 0
    return 1
    
    
def solution(places):
    answer = []
    
    for p in places:
        answer.append(bfs(p))
    
    return answer