import sys
input = sys.stdin.readline
MAX_QUERY = 2000000

seg_tree = [0] * MAX_QUERY * 4
# 세그먼트 트리는 구간, 합, 최소, 최대를 생각하고 접근하는 것이 좋음

# 1번 쿼리는 X에 해당하는 모든 노드에 +1
# 2번 쿼리는 k번째 수 X를 찾은다음 출력 -> X에 해당하는 모든 노드 -1

# https://kangwlgns.tistory.com/24

def update(X):
    while X>=1:
        seg_tree[X]+=1
        X//2

def update_remove():
    pass

n = int(input())
for i in range(n):
    t,x = map(int, input().split())
    if t==1:
        update()
    else:
        update_remove()