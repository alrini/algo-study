import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = []

    for i in range(n):
        a.append([*map(int, input().split())])

    a.sort()
    ans = 1
    min_second = a[0][1]

    for i in range(1, n):
        if a[i][1] > min_second:
            continue

        min_second = a[i][1]
        ans += 1

    print(ans)
