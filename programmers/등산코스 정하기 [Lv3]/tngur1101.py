from collections import defaultdict
from heapq import heappop, heappush

def get_min_intensity(n,gates, summits, graph):
    field = []
    summits.sort()
    set_summits = set(summits)
    visited = [10000001] * (n+1)
    
    for gate in gates:
        heappush(field, (0,gate))
        visited[gate] = 0
        
    while field:
        intensity, node = heappop(field)
        
        if node in set_summits or intensity > visited[node]:
            continue
            
        for weight, next_node in graph[node]:
            new_intensity = max(intensity, weight)
            if new_intensity < visited[next_node]:
                visited[next_node] = new_intensity
                heappush(field, (new_intensity, next_node))
                
    min_intensity = [0,10000001]
    for summit in summits:
        if visited[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]
            
    return min_intensity

def solution(n, paths, gates, summits):
    answer = []
    # n: 산의 지점 수
    # paths: 등산로의 정보 (2차원 배열)
    # gates: 출입구 번호가 있는 정수 배열 => 시작점
    # summits: 산봉우리 정수 배열 => 여기에 있는 애들만 산봉우리임
    graph = defaultdict(list)
    for i,j,w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))
        
    return get_min_intensity(n,gates, summits, graph)