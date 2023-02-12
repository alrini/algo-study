parent = [i for i in range(105)]

def disjoint_set_find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = disjoint_set_find(parent[a])
        return parent[a]

def disjoint_set_union(a, b):
    pa, pb = disjoint_set_find(a), disjoint_set_find(b)

    if pa != pb:
        parent[pa] = pb

def solution(n, costs):
    ans = 0
    costs.sort(key=lambda x: x[2])

    for cost in costs:
        if disjoint_set_find(cost[0]) == disjoint_set_find(cost[1]):
            continue

        ans += cost[2]
        disjoint_set_union(cost[0], cost[1])

    return ans