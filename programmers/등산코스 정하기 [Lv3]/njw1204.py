import sys
from collections import deque
sys.setrecursionlimit(10**6)

def disjoint_set_init(n, gates, summits):
    global parent, has_gate, has_summit
    parent = [i for i in range(n + 5)]
    has_gate = [False]*(n + 5)
    has_summit = [False]*(n + 5)

    for gate in gates:
        has_gate[gate] = True

    for summit in summits:
        has_summit[summit] = True

def disjoint_set_find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = disjoint_set_find(parent[a])
        return parent[a]

def disjoint_set_union(a, b):
    pa, pb = disjoint_set_find(a), disjoint_set_find(b)

    if pa != pb:
        has_gate[pb] = has_gate[pa] or has_gate[pb]
        has_summit[pb] = has_summit[pa] or has_summit[pb]
        parent[pa] = pb

def solution(n, paths, gates, summits):
    gates.sort()
    summits.sort()

    links = [[] for _ in range(n + 5)]
    is_gate = [False]*(n + 5)
    is_summit = [False]*(n + 5)

    for i, j, w in paths:
        links[i].append([j, w])
        links[j].append([i, w])

    for gate in gates:
        is_gate[gate] = True

    for summit in summits:
        is_summit[summit] = True

    left, right = 1, 10000000

    while left <= right:
        mid = (left + right) // 2
        disjoint_set_init(n, gates, summits)

        for i, j, w in paths:
            if w <= mid:
                disjoint_set_union(i, j)

        if left == right:
            visited = [False]*(n + 5)

            for summit in summits:
                if visited[summit] or not has_gate[disjoint_set_find(summit)]:
                    continue

                q = deque()
                q.append(summit)
                visited[summit] = True

                while q:
                    cur = q.popleft()

                    for node, dist in links[cur]:
                        if dist <= mid and not visited[node] and not is_summit[node]:
                            if is_gate[node]:
                                return [summit, mid]

                            q.append(node)
                            visited[node] = True

        ok = False

        for summit in summits:
            if has_gate[disjoint_set_find(summit)]:
                ok = True
                break

        if ok:
            right = mid
        else:
            left = mid + 1