import sys
input = sys.stdin.readline

disjoint_set = [i for i in range(100005)]

def disjoint_set_find(a):
    if disjoint_set[a] == a:
        return a

    disjoint_set[a] = disjoint_set_find(disjoint_set[a])
    return disjoint_set[a]

def disjoint_set_union(a, b):
    pa, pb = disjoint_set_find(a), disjoint_set_find(b)

    if pa == pb:
        return

    disjoint_set[pa] = pb

n, m = map(int, input().split())

for i in range(m):
    a, b = map(int, input().split())
    disjoint_set_union(a, b)

x = [*map(int, input().split())]
cur = disjoint_set_find(x[0])
ans = 0

for i in range(1, n):
    nxt = disjoint_set_find(x[i])

    if nxt != cur:
        ans += 1

    cur = nxt

print(ans)
