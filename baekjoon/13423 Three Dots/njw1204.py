for _ in range(int(input())):
    n = int(input())
    x = sorted(map(int, input().split()))
    x_set = set(x)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (x[j] - x[i]) % 2 == 0 and x[i] + (x[j] - x[i]) // 2 in x_set:
                ans += 1

    print(ans)
