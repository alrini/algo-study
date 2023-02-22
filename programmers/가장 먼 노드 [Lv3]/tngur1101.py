from collections import deque

def solution(n, edge):
    answer = 0
    edge.sort()
    distance = [0]*(n+1)
    graph = [[] for i in range(n+1)]
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
        
    queue = deque()
    queue.append(1)
    distance[1] = 1
    
    while queue:
        node = queue.popleft()
        
        for index in graph[node]:
            if not distance[index]:
                queue.append(index)
                distance[index] = distance[node]+1
                
    max_distance = max(distance)
    answer = max_distance
    
    return answer