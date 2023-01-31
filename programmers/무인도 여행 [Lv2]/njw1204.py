from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    island_count = 0
    food_of_island = [0]*10005
    visited = [[0]*105 for _ in range(105)]
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] or maps[i][j] == "X":
                continue
            
            island_count += 1
            
            q = deque()
            q.append([i, j])
            visited[i][j] = island_count
            food_of_island[island_count] += int(maps[i][j])
            
            while q:
                si, sj = q.popleft()
                
                for dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = si + dx[0], sj + dx[1]

                    if ni < 0 or ni > n - 1 or nj < 0 or nj > m - 1:
                        continue

                    if visited[ni][nj] or maps[ni][nj] == "X":
                        continue

                    q.append([ni, nj])
                    visited[ni][nj] = island_count
                    food_of_island[island_count] += int(maps[ni][nj])
    
    answer = sorted(filter(None, food_of_island))
    return answer if answer else [-1]