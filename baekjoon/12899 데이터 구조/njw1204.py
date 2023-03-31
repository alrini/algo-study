import sys
input = sys.stdin.readline

MAX_NUM = 2000000
seg = [0] * MAX_NUM * 4

def update_seg(idx, val, node, start, end):
    global seg

    if idx < start or idx > end:
        return

    if start == end:
        seg[node] += val
        return

    update_seg(idx, val, node * 2, start, (start + end) // 2)
    update_seg(idx, val, node * 2 + 1, (start + end) // 2 + 1, end)
    seg[node] = seg[node * 2] + seg[node * 2 + 1]

def query_seg(nth, node, start, end):
    global seg
    seg[node] -= 1

    if start == end:
        return start

    if seg[node * 2] >= nth:
        return query_seg(nth, node * 2, start, (start + end) // 2)
    else:
        return query_seg(nth - seg[node * 2], node * 2 + 1, (start + end) // 2 + 1, end)

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a == 1:
        update_seg(b, 1, 1, 1, MAX_NUM)
    else:
        print(query_seg(b, 1, 1, MAX_NUM))
