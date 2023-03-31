import sys
input = sys.stdin.readline

n,m = map(int, input().split())
disjoint=[0]*(n+1)

for i in range(1,n+1):
    disjoint[i] =i

def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if disjoint[x] != x:
        disjoint[x] = find(disjoint[x])
    return disjoint[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        disjoint[b] = a
    else:
        disjoint[a] = b

for i in range(m):
    l,o = map(int, input().split())
    union(l,o)

A = list(map(int, input().split()))
answer = 0

for i in range(1,len(A)):
    if find(A[i])!=find(A[i-1]):
        answer += 1

print(answer)