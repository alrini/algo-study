from collections import deque

N,M,K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dir = [[0,1],[0,-1],[1,0],[-1,0]]

answer = 0

def bfs(posy,posx):
    queue = deque
    queue.append(posy,posx)
    arr[posy][posx]=1
    cnt = 1
    while True:
        if len(queue)==0:
            break
        ny, nx = queue.pop()
        for d in dir:
            nexty, nextx = ny + d[0], nx + d[1]
            if nexty < 0 or nextx < 0 or nexty>=n or nextx>=n:
                continue
            if arr[nexty][nextx] == 1:
                continue
            arr[nexty][nextx] = 1
            cnt += 1
            queue.append(nexty,nextx)
    return cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            cnt = bfs(i,j)
            answer += int(cnt/k)
            if cnt%k != 0:
                answer += 1

if answer>M or answer == 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(M-answer)