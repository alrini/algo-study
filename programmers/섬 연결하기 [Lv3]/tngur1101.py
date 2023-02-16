def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])

def unionParent(parent, a,b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def compareParent(parent, a,b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a==b:
        return True
    else:
        return False
    
def solution(n, costs):
    answer = 0
    # 크루스칼 알고리즘 - union, find 알고리즘 응용
    cnt = 0
    
    # parent-node 초기화
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    
    # cost별로 정렬
    costs.sort(key = lambda x: x[2]) # [0,1,1]의 경우 x[2]가 cost를 의미하므로
    
    for cost in costs:
        if not compareParent(parent, cost[0], cost[1]):
            answer += cost[2]
            unionParent(parent, cost[0], cost[1])
            cnt+=1
            
        if cnt == n-1:
            break
    
    
    return answer