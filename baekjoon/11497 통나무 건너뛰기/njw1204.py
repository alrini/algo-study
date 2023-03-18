from collections import deque

for _ in range(int(input())):
    n = int(input())
    l = [*map(int, input().split())]
    dq = deque()

    l.sort(reverse=True)
    dq.append(l[0])

    for i in range(1, n, 2):
        dq.append(l[i])

        if i + 1 < n:
            dq.appendleft(l[i + 1])

    ans = 0

    for i in range(n):
        ans = max(ans, abs(dq[i] - dq[i - 1]))

    print(ans)
